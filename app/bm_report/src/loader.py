"""Loads a single Excel BM-report file into a raw long-format DataFrame."""

import functools
import itertools
import logging
import math
import pathlib
import re
from typing import Any

import pandas as pd

from src import config

_logger = logging.getLogger(__name__)

_FILENAME_RE = re.compile(
    r"^(?P<product>CDE|PJ)\s+.*_(?P<year>\d{4})_",
    re.IGNORECASE,
)


def _parse_filename(path: pathlib.Path) -> tuple[str, int]:
    """Extracts product label and year from an Excel filename.

    Args:
        path: Path to the Excel file.

    Returns:
        A (product, year) tuple, e.g. ("CDE", 2024).

    Raises:
        ValueError: If the filename does not match the expected pattern.
    """
    match = _FILENAME_RE.match(path.name)
    if not match:
        raise ValueError(
            f"Cannot infer product/year from filename: {path.name!r}. "
            "Expected pattern: '<PRODUCT> biz status_<YEAR>_...'."
        )
    return match.group("product").upper(), int(match.group("year"))


def _col_b(row: tuple[Any, ...]) -> str | None:
    """Returns the stripped string value of column B, or None if empty/NaN.

    Args:
        row: A single worksheet row as a tuple of cell values.

    Returns:
        Stripped string, or None when the cell is empty or NaN.
    """
    raw = row[1] if len(row) > 1 else None
    if raw is None or (isinstance(raw, float) and math.isnan(raw)):
        return None
    return str(raw).strip()


def _scan_step(
    state: tuple[str | None, tuple | None],
    row: tuple[Any, ...],
) -> tuple[str | None, tuple | None]:
    """Accumulate step that tracks the current rev_op_type across rows.

    Returns a (rev_op_type, data_row) pair: ``data_row`` is the original row
    when it is a data row, or None when the row should be skipped.

    Args:
        state: Previous (current_rev_op, _) pair carried forward.
        row: Current worksheet row.

    Returns:
        Updated (current_rev_op, row_or_None) pair.
    """
    current_rev_op, _ = state
    b = _col_b(row)
    if b is None:
        return (current_rev_op, None)
    if b in config.REV_OP_TYPE_HEADERS:
        return (config.REV_OP_TYPE_HEADERS[b], None)
    if b.lower() in config.SECTION_TYPE_LABELS or current_rev_op is None:
        return (current_rev_op, None)
    return (current_rev_op, row)


def _make_record(
    product: str,
    year: int,
    rev_op: str,
    row: tuple[Any, ...],
    section: tuple[str, int, int],
    month_entry: tuple[int, str],
) -> dict[str, Any] | None:
    """Builds one record dict from a single (section, month) combination.

    Args:
        product: Product label (e.g. ``"CDE"``).
        year: Report year (e.g. ``2024``).
        rev_op: Canonical rev_op_type value.
        row: Source worksheet row.
        section: ``(sales_budget_type, region_col, month_start_col)`` triple.
        month_entry: ``(month_index, month_name)`` pair.

    Returns:
        Record dict, or None if the region cell is empty.
    """
    sbt, reg_col, month_start = section
    m_idx, month_name = month_entry
    region_raw = row[reg_col] if reg_col < len(row) else None
    if region_raw is None:
        return None
    col_idx = month_start + m_idx
    raw = row[col_idx] if col_idx < len(row) else None
    return {
        "product": product,
        "year": year,
        "region": str(region_raw).strip(),
        "rev_op_type": rev_op,
        "sales_budget_type": sbt,
        "month": month_name,
        "amount": float(raw) if raw is not None else 0.0,
    }


def _expand_data_row(
    product: str,
    year: int,
    rev_op: str,
    row: tuple[Any, ...],
) -> list[dict[str, Any]]:
    """Expands one data row into records for all sections and months.

    Args:
        product: Product label.
        year: Report year.
        rev_op: Current rev_op_type.
        row: Source worksheet row.

    Returns:
        List of record dicts (up to len(SECTION_CONFIG) × 12).
    """
    combos = itertools.product(
        config.SECTION_CONFIG,
        enumerate(config.MONTH_COLS),
    )
    make = functools.partial(_make_record, product, year, rev_op, row)
    return list(filter(None, map(lambda c: make(*c), combos)))


def _parse_rows(
    rows: list[tuple[Any, ...]],
    product: str,
    year: int,
) -> list[dict[str, Any]]:
    """Converts raw worksheet rows into a flat list of record dicts.

    Uses ``itertools.accumulate`` to carry the current rev_op_type forward
    across rows without explicit mutable state.

    Args:
        rows: All cell-value tuples from one worksheet.
        product: Product label (e.g. ``"CDE"``).
        year: Report year (e.g. ``2024``).

    Returns:
        Flat list of record dicts ready to be loaded into a DataFrame.
    """
    tagged = itertools.accumulate(rows, _scan_step, initial=(None, None))
    data_rows = (
        (rev_op, row)
        for rev_op, row in tagged
        if row is not None
    )
    expand = functools.partial(_expand_data_row, product, year)
    return list(
        itertools.chain.from_iterable(
            map(lambda t: expand(*t), data_rows)
        )
    )


def load_excel(path: pathlib.Path) -> pd.DataFrame:
    """Reads one Excel BM-report file and returns a raw long-format DataFrame.

    Infers ``product`` and ``year`` from the filename, parses the multi-block
    worksheet layout, and melts the 12 month columns into individual rows.

    Args:
        path: Absolute path to the ``.xlsx`` file.

    Returns:
        DataFrame with columns:
        product, year, region, rev_op_type, sales_budget_type, month, amount.
        ``amount`` is a raw float at this stage (not yet scaled or cast).

    Raises:
        ValueError: If the filename pattern is unrecognised.
        FileNotFoundError: If ``path`` does not exist.
    """
    product, year = _parse_filename(path)
    _logger.debug("Loading %s  (product=%s, year=%d)", path.name, product, year)

    wb_df = pd.read_excel(path, sheet_name=None, header=None, engine="openpyxl")

    def _sheet_records(item: tuple[str, pd.DataFrame]) -> list[dict[str, Any]]:
        sheet_name, sheet_df = item
        rows = list(sheet_df.itertuples(index=False, name=None))
        records = _parse_rows(rows, product, year)
        _logger.debug("  sheet %r → %d records", sheet_name, len(records))
        return records

    all_records = list(
        itertools.chain.from_iterable(map(_sheet_records, wb_df.items()))
    )

    if not all_records:
        _logger.warning("No records extracted from %s", path.name)
        return pd.DataFrame(columns=config.OUTPUT_COLUMNS)

    return pd.DataFrame(all_records)
