import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

TMPL = "plotly_dark"
MONTH_ORDER = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def _sort_months(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["month"] = pd.Categorical(df["month"], categories=MONTH_ORDER, ordered=True)
    return df.sort_values("month")


def monthly_line(df: pd.DataFrame, budget_type: str = "Actual") -> go.Figure:
    sub = _sort_months(df[df["sales_budget_type"] == budget_type])
    agg = sub.groupby(["month", "region"], observed=True)["amount"].sum().reset_index()
    return px.line(
        agg, x="month", y="amount", color="region",
        template=TMPL,
        title=f"Monthly Revenue by Region ({budget_type})",
        labels={"amount": "Revenue", "month": "Month"},
        markers=True,
    )


def mom_growth_line(df: pd.DataFrame, budget_type: str = "Actual") -> go.Figure:
    sub = _sort_months(df[(df["sales_budget_type"] == budget_type) & df["mom_growth"].notna()])
    agg = sub.groupby(["month", "region"], observed=True)["mom_growth"].mean().reset_index()
    agg["mom_pct"] = agg["mom_growth"] * 100
    return px.line(
        agg, x="month", y="mom_pct", color="region",
        template=TMPL,
        title=f"MoM Growth Rate by Region ({budget_type})",
        labels={"mom_pct": "MoM Growth (%)", "month": "Month"},
        markers=True,
    )


def seasonal_heatmap(df: pd.DataFrame, budget_type: str = "Actual") -> go.Figure:
    sub = df[df["sales_budget_type"] == budget_type]
    pivot = (
        sub.groupby(["month", "region"])["seasonal_index"]
        .mean()
        .reset_index()
        .pivot(index="month", columns="region", values="seasonal_index")
        .reindex(MONTH_ORDER)
    )
    return px.imshow(
        pivot, template=TMPL,
        title=f"Seasonal Index Heatmap ({budget_type})",
        color_continuous_scale="Blues",
        text_auto=".3f",
    )
