import streamlit as st
import plotly.express as px
from src.analysis import load_data, get_avg_delivery_time, get_volume_by_location, get_delay_alerts
from src.maps_utils import get_estimated_duration

st.set_page_config(page_title="Delivery Optimization Dashboard", layout="wide")
st.title("🚚 Delivery Time Optimization Dashboard")

# Load data
df = load_data()

# Sidebar input for Google Maps API
api_key = st.sidebar.text_input("🔑 Enter your Google Maps API Key", type="password")
st.sidebar.markdown("Get your key from [Google Cloud Console](https://console.cloud.google.com/)")

# KPIs
col1, col2, col3 = st.columns(3)

with col1:
    avg_time = get_avg_delivery_time(df)
    st.metric("Average Delivery Time (min)", f"{avg_time:.2f}")

with col2:
    delayed_orders = get_delay_alerts(df)
    st.metric("Orders > 10 mins", len(delayed_orders))

with col3:
    st.metric("Total Orders", len(df))

# Charts
st.subheader("📍 Order Volume by Destination")
location_df = get_volume_by_location(df)
fig1 = px.bar(location_df, x="Location", y="Order Volume", color="Order Volume", text_auto=True)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("⏱️ Delivery Time Distribution")
fig2 = px.histogram(df, x="delivery_duration_min", nbins=25, title="Delivery Time Histogram")
st.plotly_chart(fig2, use_container_width=True)

# Google Maps comparison
if api_key:
    st.subheader("🗺️ Google Maps Duration Estimator")

    sample_row = df.sample(1).iloc[0]
    origin = sample_row["origin"]
    destination = sample_row["destination"]
    actual = sample_row["delivery_duration_min"]

    result = get_estimated_duration(api_key, origin, destination)

    col_a, col_b = st.columns(2)
    with col_a:
        st.write(f"**From:** {origin}")
        st.write(f"**To:** {destination}")
        st.write(f"**Actual Delivery:** {actual:.2f} min")

    with col_b:
        st.write(f"**Google Estimate:** {result['duration_text']}")
        if result['duration_min']:
            diff = actual - result['duration_min']
            st.write(f"**Difference:** {diff:+.2f} min")

# Data table
st.subheader("📋 Sample Data")
st.dataframe(df.sample(10))
