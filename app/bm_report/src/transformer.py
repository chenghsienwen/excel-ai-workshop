"""Normalises, validates, and reshapes a raw BM-report DataFrame."""

import functools
import logging

import pandas as pd

from src import config

_logger = logging.getLogger(__name__)

_STR_COLS = ("region", "rev_op_type", "sales_budget_type", "month", "product")

_VALIDATION_RULES = (
    ("rev_op_type", config.VALID_REV_OP_TYPES),
    ("sales_budget_type", config.VALID_SALES_BUDGET_TYPES),
)


def _validate_column(
    df: pd.DataFrame,
    column: str,
    valid_values: frozenset[str],
) -> pd.DataFrame:
    """Drops rows whose ``column`` value is not in ``valid_values``.

    Args:
        df: Input DataFrame.
        column: Name of the column to validate.
        valid_values: Accepted values for that column.

    Returns:
        Filtered DataFrame with only valid rows.
    """
    mask = df[column].isin(valid_values)
    invalid = df.loc[~mask, column].unique().tolist()
    if invalid:
        _logger.warning(
            "Dropping %d rows with unrecognised %s values: %s",
            (~mask).sum(),
            column,
            invalid,
        )
    return df.loc[mask].copy()


def _strip_str_cols(df: pd.DataFrame) -> pd.DataFrame:
    """Returns a copy of ``df`` with all string columns whitespace-stripped.

    Uses ``functools.reduce`` to apply the strip operation to each column in
    ``_STR_COLS`` in sequence.

    Args:
        df: Input DataFrame.

    Returns:
        Copy of ``df`` with string columns stripped.
    """
    return functools.reduce(
        lambda acc, col: acc.assign(**{col: acc[col].str.strip()}),
        _STR_COLS,
        df.copy(),
    )


def _apply_validations(df: pd.DataFrame) -> pd.DataFrame:
    """Applies all validation rules in sequence via ``functools.reduce``.

    Args:
        df: Input DataFrame.

    Returns:
        DataFrame with invalid rows dropped.
    """
    return functools.reduce(
        lambda acc, rule: _validate_column(acc, *rule),
        _VALIDATION_RULES,
        df,
    )


def transform(
    df: pd.DataFrame,
    product: str,
    year: int,
) -> pd.DataFrame:
    """Normalises a raw loader DataFrame into the canonical output schema.

    Steps:
    1. Strip whitespace from all string columns (via ``functools.reduce``).
    2. Validate ``rev_op_type`` and ``sales_budget_type``; drop unknown rows.
    3. Scale ``amount`` by ``AMOUNT_SCALE`` and cast to ``int``.
    4. Return only ``OUTPUT_COLUMNS`` in canonical order.

    Args:
        df: Raw DataFrame produced by ``loader.load_excel``.
        product: Product label used for log context (e.g. ``"CDE"``).
        year: Report year used for log context (e.g. ``2024``).

    Returns:
        Normalised DataFrame with columns matching ``config.OUTPUT_COLUMNS``
        and ``amount`` as ``int``.
    """
    if df.empty:
        _logger.warning(
            "%s %d: empty DataFrame, nothing to transform.", product, year
        )
        return df[config.OUTPUT_COLUMNS] if config.OUTPUT_COLUMNS[0] in df else df

    result = (
        df.pipe(_strip_str_cols)
        .pipe(_apply_validations)
        .assign(
            amount=lambda d: (
                d["amount"].fillna(0.0).mul(config.AMOUNT_SCALE).round().astype(int)
            )
        )
    )

    return result[config.OUTPUT_COLUMNS].reset_index(drop=True)
