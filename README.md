# 🚚 Supply Chain Delay Prediction System

🔗 **Live App:** https://supply-chain-optimization-ds.streamlit.app/

---

## 📌 Project Overview

This project focuses on building an **end-to-end Machine Learning system** to predict shipment delays in a supply chain using operational and logistics data.

The system analyzes factors like inventory levels, shipping time, cost, supplier, and warehouse details to estimate **expected delivery delays**, enabling better logistics planning and decision-making.

---

## 🎯 Business Problem

In supply chain operations, delays can lead to:

* Increased operational costs
* Poor customer satisfaction
* Inefficient inventory management

This project aims to **predict delay days in advance**, helping organizations:

* Optimize shipping routes
* Improve supplier selection
* Reduce delivery risks

---

## ⚙️ Tech Stack

* **Programming Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost
* **Visualization:** Matplotlib / Streamlit Charts
* **Deployment:** Streamlit Cloud
* **Version Control:** Git & GitHub

---

## 🔍 Dataset Features

The dataset includes:

* Inventory_Level
* Shipping_Time
* Shipping_Cost
* Order_Quantity
* Supplier_Name
* Product_Type
* Warehouse
* Region
* Delivery_Status
* Delay_Days (Target Variable)

---

## 🧠 Machine Learning Approach

### 1. Data Preprocessing

* Handled categorical variables using **One-Hot Encoding**
* Removed non-informative features (e.g., IDs)
* Ensured proper feature alignment for model training

---

### 2. Model Building

Two models were implemented:

* **Random Forest (Baseline)**
* **XGBoost (Final Model)**

---

### 3. Model Evaluation

Metrics used:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

👉 XGBoost performed better and was selected as the final model.

---

### 4. Feature Importance Insights

Top factors influencing delays:

* Shipping Cost
* Inventory Level
* Order Quantity

These insights help in **identifying bottlenecks** in logistics.

---

## 🚀 Deployment

The model is deployed using **Streamlit**, providing:

* Real-time delay prediction
* User-friendly input interface
* Batch prediction via CSV upload
* Visualization of input vs predicted delay

---

## 💻 How to Run Locally

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Features of the App

* 📥 User input-based prediction
* 📂 Batch CSV upload prediction
* 📈 Visualization of results
* ⚡ Fast and interactive UI

---

## 🔥 Key Highlights

* End-to-end ML pipeline (EDA → Model → Deployment)
* Real-world supply chain use case
* Model comparison and selection
* Deployed application with live predictions
* Handles categorical encoding dynamically

---

## 📈 Future Improvements

* Add real-time data integration (APIs)
* Include route and weather-based features
* Improve model performance with larger datasets
* Add dashboard analytics (Power BI / Plotly)

---

## 🙌 Author

Developed as part of an **industry-level AI/ML & Data Science portfolio project**.
