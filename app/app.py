"""
Streamlit App for Retention Decision System

Run:
streamlit run app/app.py
"""

import streamlit as st
import pandas as pd
import joblib


# Load model
model = joblib.load("models/churn_model.pkl")


# Risk logic
def assign_risk(prob):
    if prob >= 0.6:
        return "High"
    elif prob >= 0.4:
        return "Medium"
    else:
        return "Low"


# App title
st.title("Retention Decision System")

st.write("Predict customer churn and recommend retention strategy.")


# User inputs
credit_score = st.number_input("Credit Score", 300, 900, 600)
age = st.number_input("Age", 18, 100, 40)
tenure = st.number_input("Tenure (years)", 0, 10, 3)
balance = st.number_input("Balance", 0.0, 250000.0, 50000.0)
num_products = st.number_input("Number of Products", 1, 4, 2)
is_active = st.selectbox("Is Active Member", [0, 1])
estimated_salary = st.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)

# Categorical inputs
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Male", "Female"])


# Predict button
if st.button("Predict"):

    # Create dataframe
    data = pd.DataFrame({
        "creditscore": [credit_score],
        "age": [age],
        "tenure": [tenure],
        "balance": [balance],
        "numofproducts": [num_products],
        "isactivemember": [is_active],
        "estimatedsalary": [estimated_salary],
    })

    # Feature engineering (must match training)
    data["balance_per_product"] = data["balance"] / (data["numofproducts"] + 1)
    data["credit_per_age"] = data["creditscore"] / (data["age"] + 1)
    data["tenure_per_age"] = data["tenure"] / (data["age"] + 1)

    # Encode categorical variables
    data["geography_Germany"] = 1 if geography == "Germany" else 0
    data["geography_Spain"] = 1 if geography == "Spain" else 0
    data["gender_Male"] = 1 if gender == "Male" else 0

    # Ensure column order matches training
    model_columns = model.feature_names_in_
    data = data.reindex(columns=model_columns, fill_value=0)

    # Prediction
    prob = model.predict_proba(data)[0][1]
    risk = assign_risk(prob)

    if risk == "High":
        action = "Strategy A"
    else:
        action = "No Action"

    # Output
    st.subheader("Prediction Results")
    st.write(f"Churn Probability: {prob:.2f}")
    st.write(f"Risk Level: {risk}")
    st.write(f"Recommended Action: {action}")