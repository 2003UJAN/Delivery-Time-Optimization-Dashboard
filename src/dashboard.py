import streamlit as st
import plotly.express as px
from analysis import load_data, get_avg_delivery_time, get_volume_by_location, get_delay_alerts

st.set_page_config(page_title="Delivery Time Optimization", layout="wide")
st.title("🚚 Delivery Time Optimization Dashboard")

df = load_data()

col1, col2 = st.columns(2)
with col1:
    avg_time = get_avg_delivery_time(df)
    st.metric("Average Delivery Time (min)", f"{avg_time:.2f}")

with col2:
    delayed_orders = get_delay_alerts(df)
    st.metric("Orders > 10 mins", len(delayed_orders))

st.subheader("📍 Order Volume by Location")
location_df = get_volume_by_location(df)
fig = px.bar(location_df, x="Location", y="Order Volume", color="Order Volume", text_auto=True)
st.plotly_chart(fig, use_container_width=True)

st.subheader("🕐 Delivery Time Distribution")
fig2 = px.histogram(df, x="delivery_duration_min", nbins=20, title="Delivery Duration Histogram")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("📋 Detailed Data")
st.dataframe(df.head(50))

