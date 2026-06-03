"""Trend analysis functions — stub, deferred until layers 1 & 2 validated."""

import pandas as pd


def ytd_trend(df: pd.DataFrame, cohort: dict) -> pd.DataFrame:
    """Return running YTD total by month for a given cohort.

    Args:
        df: Raw monthly DataFrame from loader.load().
        cohort: Dict of cohort key values to filter on.

    Returns:
        DataFrame with columns [month, ytd_cumsum].
    """
    return pd.DataFrame()


def yoy_delta_by_month(df: pd.DataFrame, cohort: dict) -> pd.DataFrame:
    """Return month-by-month YoY delta for a given cohort.

    Args:
        df: Raw monthly DataFrame from loader.load().
        cohort: Dict of cohort key values to filter on.

    Returns:
        DataFrame with columns [month, yoy_delta].
    """
    return pd.DataFrame()


def period_momentum(df: pd.DataFrame, cohort: dict) -> pd.DataFrame:
    """Return period-over-period momentum indicators.

    Args:
        df: Raw monthly DataFrame from loader.load().
        cohort: Dict of cohort key values to filter on.

    Returns:
        DataFrame with columns [period, current, previous, delta, pct_change].
    """
    return pd.DataFrame()
