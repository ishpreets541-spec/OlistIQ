import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.title("🎯 RFM Segmentation")

df = pd.read_csv("/Users/lakshyasmac/Desktop/E-commerce dataset/archive/merged_olist.csv")

df['order_purchase_timestamp'] = pd.to_datetime(
    df['order_purchase_timestamp']
)

snapshot_date = df['order_purchase_timestamp'].max()

rfm = df.groupby('customer_unique_id').agg({

    'order_purchase_timestamp': lambda x:
        (snapshot_date - x.max()).days,

    'order_id':'nunique',

    'payment_value':'sum'

})

rfm.columns = ['Recency','Frequency','Monetary']

# ======================
# Scaling
# ======================

scaler = StandardScaler()

rfm_scaled = scaler.fit_transform(rfm)

# ======================
# KMeans
# ======================

kmeans = KMeans(
    n_clusters=4,
    random_state=42
)

rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

# ======================
# Scatter Plot
# ======================

fig = px.scatter(

    rfm,

    x='Frequency',

    y='Monetary',

    color=rfm['Cluster'].astype(str),

    size='Monetary',

    title='RFM Segments'

)
fig.update_yaxes(type="log")
st.plotly_chart(fig, use_container_width=True)

st.dataframe(rfm.head())