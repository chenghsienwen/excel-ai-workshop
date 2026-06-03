"""Period definitions and monthly aggregation logic."""

import datetime
from typing import Optional

import pandas as pd

from . import config

PERIOD_MONTHS: dict = {
    "total": config.MONTH_COLS,
    "h1":    ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "h2":    ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "q1":    ["Jan", "Feb", "Mar"],
    "q2":    ["Apr", "May", "Jun"],
    "q3":    ["Jul", "Aug", "Sep"],
    "q4":    ["Oct", "Nov", "Dec"],
}


def ytd_months(today: datetime.date) -> list:
    """Return month names from Jan through the month of today (inclusive).

    Args:
        today: Reference date.

    Returns:
        Ordered list of month abbreviations, e.g. ["Jan", "Feb", "Mar"].
    """
    return config.MONTH_COLS[: today.month]


def aggregate_periods(
    df: pd.DataFrame,
    today: Optional[datetime.date] = None,
) -> pd.DataFrame:
    """Aggregate monthly amounts into period totals per cohort.

    Args:
        df: Raw DataFrame with COHORT_KEY + month + amount columns.
        today: Reference date for YTD; defaults to datetime.date.today().

    Returns:
        DataFrame with COHORT_KEY columns plus period columns:
        total, h1, h2, q1, q2, q3, q4, ytd.
    """
    if today is None:
        today = datetime.date.today()

    ytd = ytd_months(today)

    pivoted = (
        df.pivot_table(
            index=config.COHORT_KEY,
            columns="month",
            values="amount",
            aggfunc="sum",
            fill_value=0,
        )
        .reset_index()
    )

    period_sums = dict(map(
        lambda item: (
            item[0],
            pivoted[[m for m in item[1] if m in pivoted.columns]].sum(axis=1),
        ),
        PERIOD_MONTHS.items(),
    ))

    ytd_cols = [m for m in ytd if m in pivoted.columns]
    period_sums["ytd"] = (
        pivoted[ytd_cols].sum(axis=1)
        if ytd_cols
        else pd.Series(0, index=pivoted.index)
    )

    return pivoted[config.COHORT_KEY].assign(**period_sums)
