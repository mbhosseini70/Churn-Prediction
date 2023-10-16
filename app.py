import streamlit as st
import catboost
import numpy as np
import pandas as pd
import joblib
from utils import replace_yes_no_values, encode_yes_no_values






# Define function to make predictions
def predict(data):
    processed_data = preprocessor.transform(data)
    return model.predict_proba(processed_data)[:, 1]

# Design the Streamlit app
st.title("IT Customer Churn Prediction App")

# Create sliders/widgets for user input
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", ["Yes", "No"])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure", 0, 80, 40)
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=50.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=5000.0)



# Convert SeniorCitizen from Yes/No to 1/0
SeniorCitizen = 1 if SeniorCitizen == "Yes" else 0

# Collect all user input into a dataframe
data = pd.DataFrame({
    'gender': [gender],
    'SeniorCitizen': [SeniorCitizen],
    'Partner': [Partner],
    'Dependents': [Dependents],
    'tenure': [tenure],
    'PhoneService': [PhoneService],
    'MultipleLines': [MultipleLines],
    'InternetService': [InternetService],
    'OnlineSecurity': [OnlineSecurity],
    'OnlineBackup': [OnlineBackup],
    'DeviceProtection': [DeviceProtection],
    'TechSupport': [TechSupport],
    'StreamingTV': [StreamingTV],
    'StreamingMovies': [StreamingMovies],
    'Contract': [Contract],
    'PaperlessBilling': [PaperlessBilling],
    'PaymentMethod': [PaymentMethod],
    'MonthlyCharges': [MonthlyCharges],
    'TotalCharges': [TotalCharges]
})


# Load the preprocessor and trained model
preprocessor = joblib.load('preprocessor.pkl')
model = joblib.load('catboost_model.joblib')

# Predict on button press
if st.button("Predict Churn Probability"):
    prediction = predict(data)
    if prediction[0] >= 0.5:
        st.error(f'The customer may churn with this probability: {prediction[0]:.2f} ')
    else:
        st.success(f'The customer still with you with this probability: {prediction[0]:.2f}')




