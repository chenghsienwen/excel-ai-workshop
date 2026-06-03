"""Layer 1: period aggregation per cohort."""

import datetime
from typing import Optional

import pandas as pd

from . import periods


def build(
    df: pd.DataFrame,
    today: Optional[datetime.date] = None,
) -> pd.DataFrame:
    """Build the Layer 1 period aggregation report.

    Args:
        df: Raw DataFrame from loader.load().
        today: Reference date for YTD; defaults to datetime.date.today().

    Returns:
        DataFrame with cohort key columns plus:
        total, h1, h2, q1, q2, q3, q4, ytd.
    """
    return periods.aggregate_periods(df, today=today)
