import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

TMPL = "plotly_dark"
PERIOD_COLS = ["total", "h1", "h2", "q1", "q2", "q3", "q4", "ytd"]


def period_bar(df: pd.DataFrame) -> go.Figure:
    agg = (
        df.groupby("sales_budget_type")[PERIOD_COLS]
        .sum()
        .reset_index()
        .melt(id_vars="sales_budget_type", var_name="period", value_name="amount")
    )
    return px.bar(
        agg, x="period", y="amount", color="sales_budget_type",
        barmode="group", template=TMPL,
        category_orders={"period": PERIOD_COLS},
        title="Period Aggregation: Actual vs Budget",
        labels={"amount": "Revenue", "period": "Period", "sales_budget_type": "Type"},
    )


def region_total_bar(df: pd.DataFrame) -> go.Figure:
    agg = df.groupby(["region", "sales_budget_type"])["total"].sum().reset_index()
    return px.bar(
        agg, x="region", y="total", color="sales_budget_type",
        barmode="group", template=TMPL,
        title="Total Revenue by Region",
        labels={"total": "Revenue", "region": "Region", "sales_budget_type": "Type"},
    )
