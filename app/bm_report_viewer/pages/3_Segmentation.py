import streamlit as st
from src.loader import load_all_safe
from src.sidebar import render_sidebar, filter_df
import src.charts.layer3_seg as c

st.set_page_config(page_title="Segmentation", layout="wide")

data, err = load_all_safe()
if err:
    st.error(err)
    st.stop()

filters = render_sidebar(data)
df = filter_df(data["layer3_seg"], filters)

st.title("Segmentation")

budget_type = st.radio("Type", ["Actual", "Budget"], horizontal=True)

col1, col2 = st.columns([2, 1])
with col1:
    st.plotly_chart(c.rank_bar(df, budget_type), use_container_width=True)
with col2:
    st.plotly_chart(c.treemap(df, budget_type), use_container_width=True)
