import requests
import streamlit as st
import api as api

# Function to make a prediction request
def get_prediction(data):
    print(data)
    response = requests.post('http://localhost:8000/predict', json=data)
    return response.json()

# UI setup
st.title("Credit Risk Prediction")

# Input fields
person_age = st.number_input("Age", min_value=0, max_value=100, step=1)
person_income = st.number_input("Income", min_value=0.0, step=1000.0)
person_home_ownership = st.selectbox("Home Ownership", ["RENT", "MORTGAGE", "OWN"])
person_emp_length = st.number_input("Employment Length", min_value=0.0, step=1.0)
loan_intent = st.selectbox("Loan Intent", ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT"])
loan_amnt = st.number_input("Loan Amount", min_value=0.0, step=1000.0)
loan_int_rate = st.number_input("Loan Interest Rate", min_value=0.0, step=0.1)
loan_grade = st.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F", "G"])
loan_percent_income = st.number_input("Loan Percent Income", min_value=0.0, step=0.1)
cb_person_default_on_file = st.selectbox("Default on File", ["Y", "N"])
cb_person_cred_hist_length = st.number_input("Credit History Length", min_value=0, max_value=30, step=1)

# Collect input data
data = {
    "person_age": person_age,
    "person_income": person_income,
    "person_home_ownership": person_home_ownership,
    "person_emp_length": person_emp_length,
    "loan_intent": loan_intent,
    "loan_amnt": loan_amnt,
    "loan_int_rate": loan_int_rate,
    "loan_grade": loan_grade,
    "loan_percent_income": loan_percent_income,
    "cb_person_default_on_file": cb_person_default_on_file,
    "cb_person_cred_hist_length": cb_person_cred_hist_length
}

# Predict button
if st.button("Predict"):
    prediction = get_prediction(data)
    st.write(f"Prediction: {prediction['prediction']}")