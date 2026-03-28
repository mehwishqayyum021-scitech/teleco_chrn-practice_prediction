import streamlit as st
import pandas as pd
from joblib import load

# Load the trained Random Forest model
# Ensure this file was saved in your current Colab directory in the previous step
model = load('random_forest_model.joblib')

# Create a Streamlit app
st.title("Customer Churn Prediction App")

# Input fields
st.header("Enter Customer Information")
tenure = st.number_input("Tenure (in months)", min_value=0, max_value=100, value=1)
internet_service = st.selectbox("Internet Service", ('DSL', 'Fiber optic', 'No'))
contract = st.selectbox("Contract", ('Month-to-month', 'One year', 'Two year'))
monthly_charges = st.number_input("Monthly Charges", min_value=0, max_value=200, value=50)
total_charges = st.number_input("Total Charges", min_value=0, max_value=10000, value=0)

# Map input values to numeric
label_mapping = {
    'DSL': 0, 'Fiber optic': 1, 'No': 2,
    'Month-to-month': 0, 'One year': 1, 'Two year': 2,
}
int_service_val = label_mapping[internet_service]
contract_val = label_mapping[contract]

# Make a prediction
if st.button("Predict Churn"):
    prediction = model.predict([[tenure, int_service_val, contract_val, monthly_charges, total_charges]])
    
    st.header("Prediction Result")
    if prediction[0] == 0:
        st.success("This customer is likely to stay.")
    else:
        st.error("This customer is likely to churn.")
