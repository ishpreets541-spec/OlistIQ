import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏪 Seller Scorecard")

df = pd.read_csv("/Users/lakshyasmac/Desktop/E-commerce dataset/archive/merged_olist.csv")

# ======================
# Seller Metrics
# ======================

seller = df.groupby('seller_id').agg({

    'payment_value':'sum',

    'review_score':'mean',

    'delay_days':'mean'

}).reset_index()

seller.columns = [

    'seller_id',

    'GMV',

    'Review_Score',

    'Avg_Delay'

]

# ======================
# Top Sellers
# ======================

top_sellers = seller.sort_values(
    by='GMV',
    ascending=False
).head(20)

fig = px.bar(

    top_sellers,

    x='seller_id',

    y='GMV',

    title='Top Sellers by GMV'

)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(seller.head())