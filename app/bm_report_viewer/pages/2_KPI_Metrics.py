import streamlit as st
from src.loader import load_all_safe
from src.sidebar import render_sidebar, filter_df
import src.charts.layer2 as c

st.set_page_config(page_title="KPI Metrics", layout="wide")

data, err = load_all_safe()
if err:
    st.error(err)
    st.stop()

filters = render_sidebar(data)
df = filter_df(data["layer2"], filters)

st.title("KPI Metrics")

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(c.ytd_gap_bar(df), use_container_width=True)
with col2:
    st.plotly_chart(c.budget_hit_rate_heatmap(df), use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    st.plotly_chart(c.yoy_bar(df), use_container_width=True)
with col4:
    st.plotly_chart(c.breakeven_scatter(df), use_container_width=True)
