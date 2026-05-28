import streamlit as st
import pandas as pd
import plotly.express as px

from xgboost import XGBClassifier

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

st.title("🔮 Churn / Repeat Purchase Prediction")

# =========================================
# Load Data
# =========================================

df = pd.read_csv("/Users/lakshyasmac/Desktop/E-commerce dataset/archive/merged_olist.csv")

# =========================================
# Datetime
# =========================================

df['order_purchase_timestamp'] = pd.to_datetime(
    df['order_purchase_timestamp']
)

snapshot_date = df['order_purchase_timestamp'].max()

# =========================================
# Customer Repeat Label
# =========================================

repeat = df.groupby(
    'customer_unique_id'
)['order_id'].nunique().reset_index()

repeat['repeat_customer'] = (
    repeat['order_id'] > 1
).astype(int)

# =========================================
# RFM Features
# =========================================

rfm = df.groupby('customer_unique_id').agg({

    'order_purchase_timestamp': lambda x:
        (snapshot_date - x.max()).days,

    'payment_value':'sum',

    'review_score':'mean',

    'delay_days':'mean'

})

rfm.columns = [

    'Recency',

    'Monetary',

    'Review_Score',

    'Avg_Delay'

]

rfm = rfm.reset_index()

# =========================================
# Merge Target
# =========================================

model_df = rfm.merge(

    repeat[['customer_unique_id','repeat_customer']],

    on='customer_unique_id'

)

# =========================================
# Features / Target
# =========================================

X = model_df[[

    'Recency',

    'Monetary',

    'Review_Score',

    'Avg_Delay'

]]

y = model_df['repeat_customer']

# =========================================
# Train Test Split
# =========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42

)

# =========================================
# XGBoost Model
# =========================================

positive = sum(y_train == 1)
negative = sum(y_train == 0)

scale_weight = negative / positive

model = XGBClassifier(

    n_estimators=200,

    max_depth=5,

    learning_rate=0.05,

    scale_pos_weight=scale_weight,

    random_state=42
)

model.fit(X_train, y_train)

# =========================================
# Predictions
# =========================================

pred = model.predict(X_test)

pred_prob = model.predict_proba(X_test)[:,1]

threshold = st.slider(
    "Prediction Threshold",
    0.1,
    0.9,
    0.7
)

pred = (pred_prob > threshold).astype(int)

# =========================================
# Metrics
# =========================================

accuracy = accuracy_score(y_test, pred)

precision = precision_score(y_test, pred)

recall = recall_score(y_test, pred)

f1 = f1_score(y_test, pred)

roc_auc = roc_auc_score(y_test, pred_prob)

# =========================================
# KPI Metrics
# =========================================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Accuracy",
    f"{accuracy:.2f}"
)

col2.metric(
    "Precision",
    f"{precision:.2f}"
)

col3.metric(
    "Recall",
    f"{recall:.2f}"
)

col4, col5 = st.columns(2)

col4.metric(
    "F1 Score",
    f"{f1:.2f}"
)

col5.metric(
    "ROC AUC",
    f"{roc_auc:.2f}"
)

# =========================================
# Classification Report
# =========================================

st.subheader("Classification Report")

report = classification_report(
    y_test,
    pred,
    output_dict=True
)

report_df = pd.DataFrame(report).transpose()

st.dataframe(report_df)

# =========================================
# Confusion Matrix
# =========================================

st.subheader("Confusion Matrix")

cm = confusion_matrix(y_test, pred)

cm_df = pd.DataFrame(

    cm,

    columns=['Predicted No','Predicted Yes'],

    index=['Actual No','Actual Yes']

)

st.dataframe(cm_df)

# =========================================
# Feature Importance
# =========================================

st.subheader("Feature Importance")

importance = pd.DataFrame({

    'Feature': X.columns,

    'Importance': model.feature_importances_

})

importance = importance.sort_values(
    by='Importance',
    ascending=False
)

st.dataframe(importance)

fig = px.bar(

    importance,

    x='Feature',

    y='Importance',

    title='Feature Importance'

)

st.plotly_chart(fig, use_container_width=True)

from sklearn.metrics import roc_curve
import plotly.express as px

fpr, tpr, thresholds = roc_curve(
    y_test,
    pred_prob
)

roc_df = pd.DataFrame({
    'FPR': fpr,
    'TPR': tpr
})

fig = px.line(

    roc_df,

    x='FPR',

    y='TPR',

    title='ROC Curve'

)

st.plotly_chart(fig, use_container_width=True)

import shap

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X_test)