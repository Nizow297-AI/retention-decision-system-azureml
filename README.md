# Retention Decision System

## Overview
This project builds an end-to-end retention decision system that combines machine learning and experimentation to improve customer retention.

The system:
- predicts customer churn risk
- identifies high-risk customers
- recommends the most effective retention strategy

## Problem
Customer churn leads to revenue loss and increased acquisition costs. Businesses need to:
1. identify customers at risk of leaving
2. determine which intervention is most effective

## Solution
This project combines:

### 1. Churn Prediction
- Model: Random Forest
- Predicts probability of churn
- Identifies high-risk customers

### 2. A/B Testing
- Compares two strategies (A vs B)
- Uses conversion as a proxy for engagement
- Determines statistically significant best strategy

### 3. Decision System
- Segments customers into risk levels
- Recommends targeted retention strategy

## Results
- ROC-AUC: ~0.78+
- Recall significantly improved through tuning
- Strategy A showed higher conversion with statistical significance

## Business Value
- Enables targeted retention strategies
- Improves customer engagement
- Reduces churn-related revenue loss
- Optimizes marketing interventions

## Project Structure

retention-decision-system/
├── data/
├── notebooks/
├── src/
├── models/
├── app/
├── README.md
├── requirements.txt

## How to Run

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run notebooks in order (01 → 07)
4. Run the Streamlit app:
   streamlit run app/app.py

## Key Insight
This project moves beyond prediction by combining machine learning with experimentation to support data-driven decision-making.

## Limitations
The A/B dataset is not directly linked to churn. Conversion is used as a proxy for engagement, which is assumed to influence retention behavior.

## Author
Niren Pillay
