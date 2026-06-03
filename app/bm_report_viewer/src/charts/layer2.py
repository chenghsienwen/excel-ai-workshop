import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

TMPL = "plotly_dark"
YOY_COLS = ["yoy_total", "yoy_h1", "yoy_h2", "yoy_q1", "yoy_q2", "yoy_q3", "yoy_q4"]


def ytd_gap_bar(df: pd.DataFrame) -> go.Figure:
    actual = df[df["sales_budget_type"] == "Actual"].copy()
    agg = actual.groupby("region")["ytd_gap"].sum().reset_index()
    agg["status"] = agg["ytd_gap"].map(lambda x: "Above" if x >= 0 else "Below")
    return px.bar(
        agg, x="region", y="ytd_gap", color="status",
        color_discrete_map={"Above": "#00CC96", "Below": "#EF553B"},
        template=TMPL,
        title="YTD Gap by Region (Actual)",
        labels={"ytd_gap": "YTD Gap", "region": "Region"},
    )


def budget_hit_rate_heatmap(df: pd.DataFrame) -> go.Figure:
    actual = df[df["sales_budget_type"] == "Actual"]
    pivot = (
        actual.groupby(["region", "product"])["budget_hit_rate"]
        .mean()
        .reset_index()
        .pivot(index="region", columns="product", values="budget_hit_rate")
    )
    return px.imshow(
        pivot, template=TMPL,
        title="Budget Hit Rate % (Actual — mean by region × product)",
        color_continuous_scale="RdYlGn", zmin=0, zmax=150,
        text_auto=".0f",
    )


def yoy_bar(df: pd.DataFrame) -> go.Figure:
    actual = df[(df["sales_budget_type"] == "Actual") & (df["yoy_total"] != 0)]
    agg = (
        actual.groupby("year")[YOY_COLS]
        .mean()
        .reset_index()
        .melt(id_vars="year", var_name="period", value_name="yoy")
    )
    agg["year"] = agg["year"].astype(str)
    return px.bar(
        agg, x="period", y="yoy", color="year",
        barmode="group", template=TMPL,
        title="Year-over-Year Ratio by Period (Actual, non-zero)",
        labels={"yoy": "YoY Ratio", "period": "Period", "year": "Year"},
    )


def breakeven_scatter(df: pd.DataFrame) -> go.Figure:
    actual = df[(df["sales_budget_type"] == "Actual") & df["breakeven_month"].notna()].copy()
    actual["breakeven_month"] = actual["breakeven_month"].astype(int)
    return px.strip(
        actual, x="region", y="breakeven_month", color="product",
        template=TMPL,
        title="Breakeven Month by Region & Product (Actual)",
        labels={"breakeven_month": "Breakeven Month", "region": "Region"},
    )
