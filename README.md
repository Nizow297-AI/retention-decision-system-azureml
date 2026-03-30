# Retention Decision System

## Overview
This project builds an end-to-end retention decision system using machine learning and A/B testing.

The system:
- predicts customer churn
- identifies high-risk customers
- recommends the most effective retention strategy

## Problem
Customer churn leads to revenue loss. Businesses need to:
1. identify at-risk customers
2. determine which intervention works best

## Approach
1. Churn prediction using Random Forest
2. Feature engineering to improve signal
3. A/B testing to compare strategies
4. Decision system to combine both

## Results
- Churn model ROC-AUC: ~0.78+
- Recall improved significantly through model tuning
- Strategy A showed higher conversion with statistical significance

## Business Value
- Enables targeted retention
- Improves decision-making
- Reduces unnecessary intervention cost

## Project Structure
- notebooks/ → analysis
- src/ → reusable code
- models/ → trained model
- data/ → datasets

## How to Run
1. Install requirements
2. Run notebooks in order (01 → 07)
3. Use prediction module in src/

## Key Insight
This project moves beyond prediction to decision-making by combining machine learning with experimentation.

## Limitation
A/B dataset uses conversion as a proxy for engagement rather than direct churn outcomes.