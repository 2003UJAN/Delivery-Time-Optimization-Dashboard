import streamlit as st
import plotly.express as px
from analysis import load_data, get_avg_delivery_time, get_volume_by_location, get_delay_alerts
from map_display import render_delivery_route

st.set_page_config(page_title="Delivery Optimization Dashboard", layout="wide")
st.title("🚚 Delivery Time Optimization Dashboard")

df = load_data()

# KPIs
col1, col2, col3 = st.columns(3)
with col1:
    avg_time = get_avg_delivery_time(df)
    st.metric("Avg Delivery Time (min)", f"{avg_time:.2f}")
with col2:
    delayed = get_delay_alerts(df)
    st.metric("Orders > 10 mins", len(delayed))
with col3:
    st.metric("Total Orders", len(df))

# Bar chart
st.subheader("📍 Orders by Destination")
vol_df = get_volume_by_location(df)
fig1 = px.bar(vol_df, x="Location", y="Order Volume", color="Order Volume", text_auto=True)
st.plotly_chart(fig1, use_container_width=True)

# Histogram
st.subheader("⏱️ Delivery Time Histogram")
fig2 = px.histogram(df, x="delivery_duration_min", nbins=20, title="Delivery Duration Distribution")
st.plotly_chart(fig2, use_container_width=True)

# Free Map Route
st.subheader("🗺️ Sample Delivery Route Map")
sample = df.sample(1).iloc[0]
st.write(f"**Origin:** {sample['origin']}")
st.write(f"**Destination:** {sample['destination']}")
render_delivery_route(sample['origin'], sample['destination'])

# Raw data
st.subheader("📄 Data Preview")
st.dataframe(df.sample(10))
