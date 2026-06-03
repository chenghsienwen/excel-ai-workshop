"""Layer 3 — Time-series: month-by-month trends per cohort."""

import datetime
from typing import Optional

import pandas as pd

from . import config

_MONTH_ORDER = {m: i for i, m in enumerate(config.MONTH_COLS)}
_BUDGET_KEY = ["region", "product", "year", "rev_op_type", "month"]

LAYER3_TS_COLUMNS = (
    config.COHORT_KEY
    + ["month", "amount", "mom_growth", "vs_budget", "seasonal_index"]
)


def build(raw: pd.DataFrame) -> pd.DataFrame:
    """Build the Layer 3 time-series trend report.

    For each cohort × month, computes month-over-month growth, deviation
    from Budget, and the month's share of the annual total (seasonal index).

    Args:
        raw: Raw monthly DataFrame from loader.load().

    Returns:
        DataFrame with cohort key + month + trend columns.
    """
    df = raw.copy()
    df["_month_idx"] = df["month"].map(_MONTH_ORDER)
    df = df.sort_values(config.COHORT_KEY + ["_month_idx"]).reset_index(drop=True)

    annual_total = df.groupby(config.COHORT_KEY)["amount"].transform("sum")
    df["seasonal_index"] = (
        (df["amount"] / annual_total.replace(0, float("nan")))
        .round(4)
    )

    prev_amount = df.groupby(config.COHORT_KEY)["amount"].shift(1)
    df["mom_growth"] = (
        (df["amount"] / prev_amount.replace(0, float("nan")))
        .round(4)
    )

    # Aggregate budget rows before joining — duplicate region rows (e.g. TW)
    # in the source data would otherwise fan out the merge.
    budget_monthly = (
        raw[raw["sales_budget_type"] == "Budget"]
        .groupby(_BUDGET_KEY, as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "budget_amount"})
    )
    df = df.merge(budget_monthly, on=_BUDGET_KEY, how="left")
    df["vs_budget"] = df["amount"] - df["budget_amount"]

    return df[LAYER3_TS_COLUMNS].reset_index(drop=True)
