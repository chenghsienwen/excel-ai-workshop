import streamlit as st
import pandas as pd


def render_sidebar(data: dict[str, pd.DataFrame]) -> dict:
    l1 = data["layer1"]
    all_years = sorted(l1["year"].unique().tolist())
    all_regions = sorted(l1["region"].unique().tolist())
    all_products = sorted(l1["product"].unique().tolist())
    all_rev_op_types = sorted(l1["rev_op_type"].unique().tolist())
    all_budget_types = sorted(l1["sales_budget_type"].unique().tolist())

    defaults = {
        "f_years": all_years,
        "f_regions": all_regions,
        "f_products": all_products,
        "f_rev_op_type": "All",
        "f_budget_type": "All",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

    with st.sidebar:
        st.header("Filters")
        st.multiselect("Year", all_years, key="f_years")
        st.multiselect("Region", all_regions, key="f_regions")
        st.multiselect("Product", all_products, key="f_products")
        st.selectbox("Rev Op Type", ["All"] + all_rev_op_types, key="f_rev_op_type")
        st.selectbox("Sales Budget Type", ["All"] + all_budget_types, key="f_budget_type")

    return {
        "years": st.session_state["f_years"],
        "regions": st.session_state["f_regions"],
        "products": st.session_state["f_products"],
        "rev_op_type": st.session_state["f_rev_op_type"],
        "budget_type": st.session_state["f_budget_type"],
    }


def filter_df(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    if filters["years"]:
        df = df[df["year"].isin(filters["years"])]
    if filters["regions"]:
        df = df[df["region"].isin(filters["regions"])]
    if filters["products"]:
        df = df[df["product"].isin(filters["products"])]
    if filters["rev_op_type"] != "All":
        df = df[df["rev_op_type"] == filters["rev_op_type"]]
    if filters["budget_type"] != "All":
        df = df[df["sales_budget_type"] == filters["budget_type"]]
    return df
