import streamlit as st
from src.loader import load_all_safe
from src.sidebar import render_sidebar, filter_df
import src.charts.layer1 as c

st.set_page_config(page_title="Period Summary", layout="wide")

data, err = load_all_safe()
if err:
    st.error(err)
    st.stop()

filters = render_sidebar(data)
df = filter_df(data["layer1"], filters)

st.title("Period Summary")

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(c.period_bar(df), use_container_width=True)
with col2:
    st.plotly_chart(c.region_total_bar(df), use_container_width=True)

st.subheader("Data Table")
st.dataframe(df, use_container_width=True)
