# 🚀 E-commerce Intelligence Platform

An end-to-end E-commerce Analytics and Machine Learning Platform built using the Brazilian Olist marketplace dataset. The platform combines business intelligence dashboards, customer segmentation, seller analytics, logistics performance monitoring, and predictive machine learning to generate actionable insights for data-driven decision-making.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-green)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Overview

This project simulates a real-world e-commerce analytics platform used by online marketplaces to monitor business performance, understand customer behavior, optimize logistics operations, and predict customer retention.

Built on the Olist Brazilian E-commerce dataset containing over **100,000 marketplace orders**, the platform integrates analytics, visualization, and machine learning into a production-style Streamlit application.

---

## 🎯 Key Features

### 📈 Revenue Intelligence

* Gross Merchandise Value (GMV) Analysis
* Average Order Value (AOV)
* Monthly Revenue Trends
* Year-over-Year Growth Analysis
* Seasonality Detection

### 👥 Customer Analytics

* RFM (Recency, Frequency, Monetary) Analysis
* Customer Segmentation using K-Means Clustering
* High-Value Customer Identification
* Customer Lifetime Value Insights

### 🏪 Seller Intelligence

* Top Seller Performance Analysis
* Seller Revenue Contribution
* Seller Rating Evaluation
* Marketplace Performance Scorecards

### 🚚 Logistics & Delivery Analytics

* Delivery Delay Analysis
* SLA Breach Monitoring
* Shipping Performance Metrics
* Customer Satisfaction Impact Analysis

### 🤖 Customer Retention Prediction

* XGBoost Classification Model
* Repeat Purchase Prediction
* Class Imbalance Handling
* Threshold Tuning
* Feature Importance Analysis
* ROC-AUC Evaluation

---

## 📊 Business Impact

The platform helps answer critical business questions:

* Which customer segments contribute the highest revenue?
* Which sellers drive marketplace growth?
* How do delivery delays impact customer satisfaction?
* Which customers are likely to purchase again?
* What seasonal patterns influence sales performance?

---

## 📈 Project Metrics

* Processed **100,000+ marketplace orders**
* Integrated **9 relational datasets**
* Built **5 interactive analytics modules**
* Achieved **0.84 ROC-AUC** for repeat purchase prediction
* Developed **multi-page Streamlit dashboards**
* Containerized deployment using **Docker**

---

## 🛠️ Tech Stack

### Programming & Analytics

* Python
* Pandas
* NumPy

### Visualization

* Plotly
* Streamlit

### Machine Learning

* Scikit-Learn
* XGBoost

### Deployment

* Docker
* Streamlit Community Cloud

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
Ecommerce-intelligence-platform/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── .gitignore
│
├── archive/
│   └── merged_olist.csv
│
├── pages/
│   ├── Revenue_Analysis.py
│   ├── RFM_Segmentation.py
│   ├── Delivery_Performance.py
│   ├── Seller_Scorecard.py
│   └── Churn_Prediction.py
│
├── models/
│   └── xgboost_model.pkl
│
└── screenshots/
```

---

## 🖥️ Dashboard Modules

### Revenue Analytics

Monitor GMV, AOV, monthly revenue trends, and growth metrics.

### Customer Segmentation

Identify customer cohorts using RFM analysis and clustering techniques.

### Seller Performance

Track top-performing sellers and marketplace contribution.

### Delivery Analytics

Analyze delivery delays, logistics efficiency, and SLA compliance.

### Retention Prediction

Predict repeat purchases using machine learning and customer behavior signals.

---

## 🚀 Running Locally

### Clone Repository

```bash
git clone https://github.com/lakshya-vipassana/Ecommerce-intelligence-platform.git
cd Ecommerce-intelligence-platform
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## 🐳 Docker Deployment

### Build Image

```bash
docker build -t ecommerce-intelligence-platform .
```

### Run Container

```bash
docker run -p 8501:8501 ecommerce-intelligence-platform
```

Application will be available at:

```text
http://localhost:8501
```

## 📚 Dataset

Brazilian E-Commerce Public Dataset by Olist

The dataset contains information about:

* Customers
* Orders
* Payments
* Reviews
* Products
* Sellers
* Logistics
* Geolocation

Source: Kaggle – Olist Brazilian E-Commerce Dataset

---

## 🔮 Future Enhancements

* SHAP Explainability
* Customer Lifetime Value Prediction
* Real-Time Analytics Pipeline
* MLflow Model Tracking
* PostgreSQL Data Warehouse
* FastAPI Prediction Service
* CI/CD Deployment Pipeline

# 👩‍💻 Author

**Ishpreet Singh**

M.Tech
Indian Institute of Technology Bombay
Mail ID:
25m0326@iitb.ac.in



---

