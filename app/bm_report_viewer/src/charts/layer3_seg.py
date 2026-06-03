import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

TMPL = "plotly_dark"


def rank_bar(df: pd.DataFrame, budget_type: str = "Actual") -> go.Figure:
    sub = df[df["sales_budget_type"] == budget_type].copy()
    sub = sub.sort_values("rank_total")
    sub["label"] = sub["region"] + " / " + sub["product"]
    return px.bar(
        sub, y="label", x="total", orientation="h",
        template=TMPL,
        title=f"Revenue Ranking ({budget_type})",
        labels={"total": "Revenue", "label": "Region / Product"},
        color="total", color_continuous_scale="Blues",
    )


def treemap(df: pd.DataFrame, budget_type: str = "Actual") -> go.Figure:
    sub = df[df["sales_budget_type"] == budget_type]
    return px.treemap(
        sub, path=["product", "region"], values="total",
        color="share_pct", template=TMPL,
        title=f"Revenue Share by Product / Region ({budget_type})",
        color_continuous_scale="Blues",
        hover_data={"ytd_gap": True, "ytd": True},
    )
