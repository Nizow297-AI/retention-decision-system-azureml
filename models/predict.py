"""
Prediction module

Purpose:
- Load trained model
- Predict churn probability
- Assign risk level
- Recommend action
"""

import joblib
import pandas as pd


# Load model once
model = joblib.load("models/churn_model.pkl")


def assign_risk(prob):
    if prob >= 0.6:
        return "High"
    elif prob >= 0.4:
        return "Medium"
    else:
        return "Low"


def predict_customer(data: pd.DataFrame) -> dict:
    """
    Predict churn for a single customer.

    Parameters
    ----------
    data : pd.DataFrame
        Customer input data

    Returns
    -------
    dict
        Prediction results
    """

    prob = model.predict_proba(data)[0][1]
    risk = assign_risk(prob)

    if risk == "High":
        action = "Strategy A"
    else:
        action = "No Action"

    return {
        "churn_probability": prob,
        "risk_level": risk,
        "recommended_action": action
    }