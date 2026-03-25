import streamlit as st
import pandas as pd
import plotly.express as px

import config
from utils import load_data, compute_kpis

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Delivery IQ", layout="wide")

# -------------------------------
# Header
# -------------------------------
st.markdown(
    "<h1 style='text-align: center;'>🚚 Delivery IQ</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align: center; color: gray;'>Food Delivery Analytics Dashboard</h4>",
    unsafe_allow_html=True
)

st.markdown("---")

# -------------------------------
# Load Data
# -------------------------------
df = load_data(config.DATA_PATH)

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("🔍 Filters")

time_filter = st.sidebar.multiselect(
    "Select Time of Day",
    options=df['Time_of_Day'].unique(),
    default=df['Time_of_Day'].unique(),
    key="time_filter"
)

traffic_filter = st.sidebar.multiselect(
    "Select Traffic Level",
    options=df['Traffic_Level'].unique(),
    default=df['Traffic_Level'].unique(),
    key="traffic_filter"
)

vehicle_filter = st.sidebar.multiselect(
    "Select Vehicle Type",
    options=df['Vehicle_Type'].unique(),
    default=df['Vehicle_Type'].unique(),
    key="vehicle_filter"
)

# Apply filters
df_filtered = df[
    (df['Time_of_Day'].isin(time_filter)) &
    (df['Traffic_Level'].isin(traffic_filter)) &
    (df['Vehicle_Type'].isin(vehicle_filter))
]

# -------------------------------
# Tabs
# -------------------------------
tab1, tab2 = st.tabs(["📊 Overview", "🔍 Advanced Insights"])

# ===============================
# 📊 TAB 1: OVERVIEW
# ===============================
with tab1:

    total_orders, avg_delivery_time, delay_percentage = compute_kpis(df_filtered)

    col1, col2, col3 = st.columns(3)

    col1.metric("📦 Total Orders", total_orders)
    col2.metric("⏱ Avg Delivery Time (min)", f"{avg_delivery_time:.2f}")
    col3.metric("⚠️ Delay %", f"{delay_percentage:.2f}%")

    st.subheader("📈 Delivery Time by Distance")

    fig1 = px.scatter(
        df_filtered,
        x="Distance_km",
        y="Delivery_Time_min",
        color="Traffic_Level",
        title="Distance vs Delivery Time"
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📊 Delay Rate by Time of Day")

    delay_time = df_filtered.groupby("Time_of_Day")['delay_flag'].mean().reset_index()

    fig2 = px.bar(
        delay_time,
        x="Time_of_Day",
        y="delay_flag",
        title="Delay Rate by Time of Day"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ===============================
# 🔍 TAB 2: ADVANCED INSIGHTS
# ===============================
with tab2:

    st.subheader("🚗 Impact of Traffic on Delivery Time")

    traffic_plot = px.box(
        df_filtered,
        x="Traffic_Level",
        y="Delivery_Time_min",
        title="Traffic vs Delivery Time"
    )
    st.plotly_chart(traffic_plot, use_container_width=True)

    st.subheader("🚴 Vehicle Performance")

    vehicle_plot = px.bar(
        df_filtered.groupby("Vehicle_Type")['Delivery_Time_min'].mean().reset_index(),
        x="Vehicle_Type",
        y="Delivery_Time_min",
        title="Avg Delivery Time by Vehicle Type"
    )
    st.plotly_chart(vehicle_plot, use_container_width=True)

    st.subheader("📊 Distance Category Analysis")

    if "distance_category" in df_filtered.columns:
        dist_plot = px.bar(
            df_filtered.groupby("distance_category")['Delivery_Time_min'].mean().reset_index(),
            x="distance_category",
            y="Delivery_Time_min",
            title="Delivery Time by Distance Category"
        )
        st.plotly_chart(dist_plot, use_container_width=True)

    # Insights
    st.subheader("💡 Key Insights")

    total_orders, avg_delivery_time, delay_percentage = compute_kpis(df_filtered)

    st.markdown(f"""
    - Average delivery time is **{avg_delivery_time:.2f} minutes**
    - Around **{delay_percentage:.2f}%** of orders are delayed
    - High traffic significantly increases delivery time
    - Longer distances tend to increase delays
    """)