"""Layer 3 — Segmentation: regional ranking within each segment."""

import pandas as pd

from . import config

_SEGMENT_KEY = ["product", "year", "rev_op_type", "sales_budget_type"]
_CROSS_KEY = ["region", "product", "year", "rev_op_type"]

LAYER3_SEG_COLUMNS = (
    _SEGMENT_KEY
    + ["region", "total", "ytd", "ytd_gap", "rank_total", "rank_ytd_gap", "share_pct"]
)


def build(layer1: pd.DataFrame) -> pd.DataFrame:
    """Build the Layer 3 segmentation ranking report.

    Ranks each region within its segment (product × year × rev_op_type ×
    sales_budget_type) by total revenue, YTD gap, and revenue share.

    Args:
        layer1: Output of layer1.build().

    Returns:
        DataFrame with segment key + region + ranking columns.
    """
    budget_ytd = (
        layer1[layer1["sales_budget_type"] == "Budget"]
        [_CROSS_KEY + ["ytd"]]
        .rename(columns={"ytd": "budget_ytd"})
    )
    df = layer1.merge(budget_ytd, on=_CROSS_KEY, how="left")
    df["ytd_gap"] = df["ytd"] - df["budget_ytd"]
    df = df.drop(columns=["budget_ytd"])

    df["rank_total"] = (
        df.groupby(_SEGMENT_KEY)["total"]
        .rank(method="dense", ascending=False)
        .astype(int)
    )

    segment_total = df.groupby(_SEGMENT_KEY)["total"].transform("sum")
    df["share_pct"] = (
        (df["total"] / segment_total.replace(0, float("nan")) * 100)
        .round(2)
    )

    df["rank_ytd_gap"] = (
        df.groupby(_SEGMENT_KEY)["ytd_gap"]
        .rank(method="dense", ascending=True)
        .astype(int)
    )

    return df[LAYER3_SEG_COLUMNS].reset_index(drop=True)
