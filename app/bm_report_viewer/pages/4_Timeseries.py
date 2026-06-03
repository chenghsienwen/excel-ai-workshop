import streamlit as st
from src.loader import load_all_safe
from src.sidebar import render_sidebar, filter_df
import src.charts.layer3_ts as c

st.set_page_config(page_title="Timeseries", layout="wide")

data, err = load_all_safe()
if err:
    st.error(err)
    st.stop()

filters = render_sidebar(data)
df = filter_df(data["layer3_ts"], filters)

st.title("Timeseries")

budget_type = st.radio("Type", ["Actual", "Budget"], horizontal=True)

st.plotly_chart(c.monthly_line(df, budget_type), use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(c.mom_growth_line(df, budget_type), use_container_width=True)
with col2:
    st.plotly_chart(c.seasonal_heatmap(df, budget_type), use_container_width=True)
