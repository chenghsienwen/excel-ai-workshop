import streamlit as st
from src.loader import load_all_safe
from src.sidebar import render_sidebar, filter_df

st.set_page_config(page_title="BM Report Viewer", layout="wide", page_icon="📊")

data, err = load_all_safe()
if err:
    st.error(f"**Input data not found.**\n\n{err}")
    st.stop()

filters = render_sidebar(data)

l1 = filter_df(data["layer1"], filters)
l2 = filter_df(data["layer2"], filters)

actual_l1 = l1[l1["sales_budget_type"] == "Actual"]
budget_l1 = l1[l1["sales_budget_type"] == "Budget"]
actual_l2 = l2[l2["sales_budget_type"] == "Actual"]

total_actual = int(actual_l1["total"].sum())
total_budget = int(budget_l1["total"].sum())
hit_rate = round(total_actual / total_budget * 100, 1) if total_budget else 0
ytd_gap = int(actual_l2["ytd_gap"].sum())

st.title("BM Report Viewer")
st.caption("Use the sidebar filters then navigate to a report page.")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Actual Revenue", f"{total_actual:,}")
c2.metric("Total Budget", f"{total_budget:,}")
c3.metric("Budget Achievement", f"{hit_rate}%")
c4.metric("YTD Gap", f"{ytd_gap:,}", delta_color="normal")
