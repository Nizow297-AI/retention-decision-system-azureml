# System Logic

## Stage 1: Churn Prediction
A churn model is trained on customer-level banking data to estimate the probability that a customer will churn.

Output:
- churn probability score for each customer
- identification of high-risk customers based on a threshold

## Stage 2: Retention Strategy Evaluation
A/B testing data is used to compare the effectiveness of two interventions.

Output:
- performance comparison between treatment A and treatment B
- statistical significance testing
- recommended strategy

## Final Decision Logic
The system combines both stages conceptually:
1. Score customers for churn risk
2. Identify high-risk segment
3. Recommend the best-performing intervention for that segment

## Business Interpretation
This project demonstrates how predictive modeling and experimentation can be combined to support targeted retention strategy rather than prediction alone.