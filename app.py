import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Supply Chain Optimization", layout="wide")

# Load model and columns
model = pickle.load(open('model_supply.pkl', 'rb'))
columns = pickle.load(open('supply_columns.pkl', 'rb'))

st.title("🚚 Supply Chain Delay Prediction")
st.markdown("---")

# ------------------- INPUT SECTION -------------------
st.subheader("Enter Shipment Details")

col1, col2 = st.columns(2)

with col1:
    inventory = st.number_input("Inventory Level", value=100)
    shipping_time = st.number_input("Shipping Time", value=5)
    shipping_cost = st.number_input("Shipping Cost", value=200)
    order_qty = st.number_input("Order Quantity", value=50)

with col2:
    supplier = st.selectbox("Supplier", ["Supplier A", "Supplier B", "Supplier C", "Supplier D"])
    product = st.selectbox("Product Type", ["Electronics", "Furniture", "Clothing", "Food"])
    warehouse = st.selectbox("Warehouse", ["Warehouse 1", "Warehouse 2", "Warehouse 3"])
    region = st.selectbox("Region", ["North", "South", "East", "West"])
    status = st.selectbox("Delivery Status", ["Delivered", "Delayed", "In Transit"])

# ------------------- PREDICTION -------------------
if st.button("Predict Delay"):
    input_dict = {
        'Inventory_Level': inventory,
        'Shipping_Time': shipping_time,
        'Shipping_Cost': shipping_cost,
        'Order_Quantity': order_qty
    }

    for col in columns:
        if 'Supplier_Name_' in col:
            input_dict[col] = 1 if col == f"Supplier_Name_{supplier}" else 0
        elif 'Product_Type_' in col:
            input_dict[col] = 1 if col == f"Product_Type_{product}" else 0
        elif 'Warehouse_' in col:
            input_dict[col] = 1 if col == f"Warehouse_{warehouse}" else 0
        elif 'Region_' in col:
            input_dict[col] = 1 if col == f"Region_{region}" else 0
        elif 'Delivery_Status_' in col:
            input_dict[col] = 1 if col == f"Delivery_Status_{status}" else 0

    input_df = pd.DataFrame([input_dict])
    input_df = input_df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(input_df)[0]

    st.success(f"⏱ Predicted Delay: {prediction:.2f} days")

    # Chart
    chart_data = pd.DataFrame({
        "Metric": ["Inventory", "Shipping Time", "Cost", "Prediction"],
        "Value": [inventory, shipping_time, shipping_cost, prediction]
    })
    st.bar_chart(chart_data.set_index("Metric"))

# ------------------- BATCH PREDICTION -------------------
st.markdown("---")
st.subheader("📂 Batch Prediction")

file = st.file_uploader("Upload CSV", type=["csv"])

if file is not None:
    data = pd.read_csv(file)
    data = data.reindex(columns=columns, fill_value=0)

    preds = model.predict(data)
    data['Predicted_Delay'] = preds

    st.write(data.head())

    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button("Download Results", csv, "supply_results.csv")
