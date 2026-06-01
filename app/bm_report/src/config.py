"""Centralised constants, paths, and utilities for bm_report."""

import contextlib
import logging
import pathlib
import time
from typing import Generator

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

_SRC_DIR = pathlib.Path(__file__).parent
BM_REPORT_DIR = _SRC_DIR.parent
RAW_DATA_DIR = BM_REPORT_DIR / "raw_data"
OUTPUT_DIR = BM_REPORT_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "raw_report.csv"

# ---------------------------------------------------------------------------
# Output schema
# ---------------------------------------------------------------------------

OUTPUT_COLUMNS = [
    "product",
    "year",
    "region",
    "rev_op_type",
    "sales_budget_type",
    "month",
    "amount",
]

MONTH_COLS = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]

SORT_COLUMNS = [
    "product",
    "year",
    "region",
    "rev_op_type",
    "sales_budget_type",
    "month",
]

# ---------------------------------------------------------------------------
# Excel structure
# ---------------------------------------------------------------------------

# Maps the value in colB of a header row to the canonical rev_op_type label.
REV_OP_TYPE_HEADERS = {
    "Gross Sales ($K)": "Gross",
    "Net Sales ($K)": "Net",
    "OP Sales ($K)": "Op",
}

# (sales_budget_type, region_col_index, month_start_col_index) — 0-based.
SECTION_CONFIG = [
    ("Actual",   1,  2),
    ("Forecast", 16, 17),
    ("Budget",   31, 32),
]

# colB values that mark a section-type header row (not data).
SECTION_TYPE_LABELS = frozenset({"actual", "forecast", "budget"})

# Recognised product prefixes extracted from filenames.
PRODUCT_PREFIXES = ("CDE", "PJ")

# Scale factor: Excel values × AMOUNT_SCALE → integer amount in output.
AMOUNT_SCALE = 10_000

# ---------------------------------------------------------------------------
# Validation sets
# ---------------------------------------------------------------------------

VALID_REV_OP_TYPES = frozenset(REV_OP_TYPE_HEADERS.values())
VALID_SALES_BUDGET_TYPES = frozenset(sbt for sbt, _, _ in SECTION_CONFIG)

# ---------------------------------------------------------------------------
# Timing utility
# ---------------------------------------------------------------------------


@contextlib.contextmanager
def timed(label: str) -> Generator[None, None, None]:
    """Context manager that logs wall-clock time for a named stage.

    Args:
        label: Human-readable stage name shown in log output.

    Yields:
        None
    """
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    logging.info("[timing] %-40s %.3f s", label, elapsed)
