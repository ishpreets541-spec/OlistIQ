import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🚚 Delivery Performance")

df = pd.read_csv("archive/merged_olist.csv")

df['order_delivered_customer_date'] = pd.to_datetime(
    df['order_delivered_customer_date']
)

df['order_estimated_delivery_date'] = pd.to_datetime(
    df['order_estimated_delivery_date']
)

# ======================
# Delay Days
# ======================

df['delay_days'] = (

    df['order_delivered_customer_date']

    -

    df['order_estimated_delivery_date']

).dt.days

# ======================
# SLA Breach
# ======================

df['sla_breach'] = df['delay_days'] > 0

sla_rate = (
    df['sla_breach'].mean()
) * 100

st.metric(
    label='SLA Breach Rate',
    value=f'{sla_rate:.2f}%'
)

# ======================
# Delay Histogram
# ======================

fig = px.histogram(

    df,

    x='delay_days',

    title='Delivery Delay Distribution'

)

st.plotly_chart(fig, use_container_width=True)

# ======================
# Delay vs Review Score
# ======================

fig2 = px.scatter(

    df,

    x='delay_days',

    y='review_score',

    title='Delay vs Review Score'

)

st.plotly_chart(fig2, use_container_width=True)
