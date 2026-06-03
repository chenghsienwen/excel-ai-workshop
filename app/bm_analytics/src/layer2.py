"""Layer 2: derived metrics (YTD gap, budget hit rate, YoY, breakeven)."""

import itertools
from typing import Optional

import pandas as pd

from . import config

_CROSS_KEY = ["region", "product", "year", "rev_op_type"]
_YOY_PERIODS = ["total", "h1", "h2", "q1", "q2", "q3", "q4"]

LAYER2_COLUMNS = (
    config.COHORT_KEY
    + ["ytd_gap", "budget_hit_rate"]
    + [f"yoy_{p}" for p in _YOY_PERIODS]
    + ["breakeven_month"]
)


def _attach_ytd_metrics(layer1: pd.DataFrame) -> pd.DataFrame:
    """Add ytd_gap and budget_hit_rate by joining against Budget YTD."""
    budget_ytd = (
        layer1[layer1["sales_budget_type"] == "Budget"]
        [_CROSS_KEY + ["ytd"]]
        .rename(columns={"ytd": "budget_ytd"})
    )
    merged = layer1.merge(budget_ytd, on=_CROSS_KEY, how="left")
    merged["ytd_gap"] = merged["ytd"] - merged["budget_ytd"]
    merged["budget_hit_rate"] = (
        (merged["ytd"] / merged["budget_ytd"].replace(0, float("nan")) * 100)
        .round(0)
        .astype("Int64")
    )
    return merged.drop(columns=["budget_ytd"])


def _attach_yoy(layer1: pd.DataFrame) -> pd.DataFrame:
    """Add yoy_* columns by self-joining across consecutive years."""
    prev = (
        layer1
        .assign(year=layer1["year"].astype(int).add(1).astype(str))
        [config.COHORT_KEY + _YOY_PERIODS]
        .rename(columns={p: f"prev_{p}" for p in _YOY_PERIODS})
    )
    merged = layer1.merge(prev, on=config.COHORT_KEY, how="left")

    def _safe_ratio(col: str) -> pd.Series:
        prev_col = merged[f"prev_{col}"].replace(0, float("nan"))
        return (merged[col] / prev_col).fillna(0).round(4)

    yoy_cols = {f"yoy_{p}": _safe_ratio(p) for p in _YOY_PERIODS}
    return merged.drop(columns=[f"prev_{p}" for p in _YOY_PERIODS]).assign(**yoy_cols)


def _compute_breakeven(raw: pd.DataFrame) -> pd.DataFrame:
    """Return a DataFrame mapping each cross-key cohort to breakeven_month.

    breakeven_month is the first month index (1=Jan … 12=Dec) where
    cumulative Actual >= cumulative Budget, or None if it never occurs.

    Args:
        raw: Raw monthly DataFrame from loader.load().

    Returns:
        DataFrame with _CROSS_KEY + breakeven_month columns.
    """
    def _pivot(sbt: str) -> pd.DataFrame:
        return (
            raw[raw["sales_budget_type"] == sbt]
            .pivot_table(
                index=_CROSS_KEY,
                columns="month",
                values="amount",
                aggfunc="sum",
                fill_value=0,
            )
            .reset_index()
        )

    actual_piv = _pivot("Actual")
    budget_piv = _pivot("Budget")
    merged = actual_piv.merge(
        budget_piv, on=_CROSS_KEY, suffixes=("_a", "_b"), how="inner"
    )

    def _find_month(row: pd.Series) -> Optional[int]:
        cum_a = itertools.accumulate(
            row.get(f"{m}_a", 0) for m in config.MONTH_COLS
        )
        cum_b = itertools.accumulate(
            row.get(f"{m}_b", 0) for m in config.MONTH_COLS
        )
        return next(
            (i + 1 for i, (a, b) in enumerate(zip(cum_a, cum_b)) if a >= b),
            None,
        )

    merged["breakeven_month"] = merged.apply(_find_month, axis=1)
    return merged[_CROSS_KEY + ["breakeven_month"]]


def build(layer1: pd.DataFrame, raw: pd.DataFrame) -> pd.DataFrame:
    """Build the Layer 2 derived metrics report.

    Args:
        layer1: Output of layer1.build().
        raw: Original raw DataFrame from loader.load().

    Returns:
        DataFrame with cohort key columns plus:
        ytd_gap, budget_hit_rate, yoy_total, yoy_h1, yoy_h2,
        yoy_q1, yoy_q2, yoy_q3, yoy_q4, breakeven_month.
    """
    result = _attach_ytd_metrics(layer1)
    result = _attach_yoy(result)

    breakeven = _compute_breakeven(raw)
    result = result.merge(breakeven, on=_CROSS_KEY, how="left")

    non_actual = result["sales_budget_type"] != "Actual"
    result.loc[non_actual, "breakeven_month"] = pd.NA

    return result[LAYER2_COLUMNS]
