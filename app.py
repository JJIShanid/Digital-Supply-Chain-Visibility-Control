 
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Digital Supply Chain Visibility & Control (SCVC)")
st.subheader("Inventory • Delivery Performance • Supply Planning • Executive KPIs")
 
df = pd.read_csv("scvc_operational_data.csv")
forecast = pd.read_csv("scvc_forecast_data.csv")
kpis = pd.read_csv("scvc_kpis.csv")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Avg Delivery Time (Days)", kpis["Avg Delivery Time"][0])
c2.metric("On-Time Delivery %", f"{kpis['On-Time Delivery %'][0]}%")
c3.metric("Total Inventory Value", f"€{kpis['Total Inventory Value'][0]:,.0f}")
c4.metric("Forecast Accuracy", f"{kpis['Forecast Accuracy %'][0]}%")

st.header("Inventory Visibility")

inventory_chart = px.line(
    df.groupby("invoicedate")["inventory_on_hand"].mean().reset_index(),
    x="invoicedate",
    y="inventory_on_hand",
    title="Average Inventory Level Over Time"
)
st.plotly_chart(inventory_chart, use_container_width=True)

stock_status = df["stock_status"].value_counts().reset_index()
stock_pie = px.pie(
    stock_status,
    values="count",
    names="stock_status",
    title="Stock Health Distribution"
)
st.plotly_chart(stock_pie, use_container_width=True)

st.header("Delivery & Order Performance")

delivery_bar = px.bar(
    df["delivery_status"].value_counts().reset_index(),
    x="delivery_status",
    y="count",
    title="On-Time vs Delayed Deliveries"
)
st.plotly_chart(delivery_bar, use_container_width=True)

st.header("Supply Planning & Demand Forecast")

forecast_chart = px.line(
    forecast,
    x="invoicedate",
    y=["sales", "forecast_sales"],
    labels={"value":"Sales (€)", "variable":"Legend"},
    title="Actual vs Forecast Sales"
)
st.plotly_chart(forecast_chart, use_container_width=True)

st.header("Supplier Performance Overview")

supplier_perf = (
    df.groupby("supplier_id")
    .agg({
        "delivery_status": lambda x: (x=="On-Time").mean()*100,
        "sales":"sum"
    })
    .reset_index()
)

supplier_chart = px.bar(
    supplier_perf,
    x="supplier_id",
    y="delivery_status",
    title="On-Time Delivery % by Supplier"
)
st.plotly_chart(supplier_chart, use_container_width=True)
