import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Revenue Trends")

df = pd.read_csv("/Users/lakshyasmac/Desktop/E-commerce dataset/archive/merged_olist.csv")

df['order_purchase_timestamp'] = pd.to_datetime(
    df['order_purchase_timestamp']
)

df['year_month'] = (
    df['order_purchase_timestamp']
    .dt.to_period('M')
    .astype(str)
)

# ======================
# Monthly GMV
# ======================

monthly_gmv = df.groupby(
    'year_month'
)['payment_value'].sum().reset_index()

fig = px.line(
    monthly_gmv,
    x='year_month',
    y='payment_value',
    title='Monthly GMV'
)

st.plotly_chart(fig, use_container_width=True)

# ======================
# AOV
# ======================

aov = df.groupby('year_month').agg({
    'payment_value':'sum',
    'order_id':'nunique'
}).reset_index()

aov['AOV'] = (
    aov['payment_value']
    /
    aov['order_id']
)

fig2 = px.bar(
    aov,
    x='year_month',
    y='AOV',
    title='Average Order Value'
)

st.plotly_chart(fig2, use_container_width=True)

# ======================
# YoY Growth
# ======================

monthly_gmv['YoY_Growth_%'] = (
    monthly_gmv['payment_value']
    .pct_change(12)
) * 100

fig3 = px.line(
    monthly_gmv,
    x='year_month',
    y='YoY_Growth_%',
    title='YoY Growth %'
)

st.plotly_chart(fig3, use_container_width=True)