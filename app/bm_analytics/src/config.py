"""Centralised constants, paths, and utilities for bm_analytics."""

import contextlib
import logging
import pathlib
import time
from typing import Generator

_SRC_DIR = pathlib.Path(__file__).parent
BM_ANALYTICS_DIR = _SRC_DIR.parent
INPUT_FILE = BM_ANALYTICS_DIR / "input" / "raw_report.csv"
OUTPUT_DIR = BM_ANALYTICS_DIR / "output"
LAYER1_FILE = OUTPUT_DIR / "layer1_report.csv"
LAYER2_FILE = OUTPUT_DIR / "layer2_report.csv"

MONTH_COLS = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]

COHORT_KEY = [
    "region",
    "product",
    "year",
    "rev_op_type",
    "sales_budget_type",
]

INPUT_COLUMNS = [
    "product",
    "year",
    "region",
    "rev_op_type",
    "sales_budget_type",
    "month",
    "amount",
]

VALID_REV_OP_TYPES = frozenset({"Gross", "Net", "Op"})
VALID_SALES_BUDGET_TYPES = frozenset({"Actual", "Budget", "Forecast"})


@contextlib.contextmanager
def timed(label: str) -> Generator[None, None, None]:
    """Log wall-clock time for a named stage.

    Args:
        label: Human-readable stage name shown in log output.

    Yields:
        None
    """
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    logging.info("[timing] %-30s %.3f s", label, elapsed)
