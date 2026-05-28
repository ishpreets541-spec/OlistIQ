# ==============================
# app.py
# ==============================

import streamlit as st

st.set_page_config(
    page_title="Olist Intelligence Platform",
    layout="wide"
)

st.title("🛒 Olist E-commerce Intelligence Platform")

st.markdown("""
## Dashboard Modules

- Revenue Trends
- RFM Segmentation
- Delivery Performance
- Seller Scorecard
- Churn Prediction
""")


st.sidebar.success("Select a page")