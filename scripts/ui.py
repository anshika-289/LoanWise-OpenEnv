import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from app.env import LoanApprovalEnv
from app.models import LoanAction

st.set_page_config(page_title="LoanWise AI", layout="centered")

st.title(" LoanWise AI - Loan Approval System")
st.write("Simulate AI-based loan underwriting decisions")

# -------------------------------
# Input Section
# -------------------------------
st.header(" Enter Loan Details")

age = st.slider("Age", 18, 65, 30)
income = st.number_input("Income (₹)", value=800000)
credit_score = st.slider("Credit Score", 300, 900, 700)

employment_status = st.selectbox(
    "Employment Status",
    ["salaried", "self_employed", "unemployed"]
)

years_employed = st.slider("Years Employed", 0, 20, 3)

loan_amount = st.number_input("Loan Amount (₹)", value=300000)
loan_purpose = st.selectbox(
    "Loan Purpose",
    ["personal", "car", "home", "business"]
)

existing_debt = st.number_input("Existing Debt (₹)", value=100000)
dti = st.slider("Debt-to-Income Ratio", 0.0, 1.0, 0.3)

repayment_history = st.selectbox(
    "Repayment History",
    ["good", "average", "poor"]
)

fraud_flag = st.selectbox("Fraud Flag", [0, 1])
documents_complete = st.selectbox("Documents Complete", [0, 1])

task_type = st.selectbox(
    "Task Type",
    ["risk", "decision", "workflow"]
)

# -------------------------------
# Prediction Button
# -------------------------------
if st.button(" Run AI Decision"):

    # Create environment manually
    env = LoanApprovalEnv()

    # Inject custom input as current case
    env.current = {
        "application_id": "USER_INPUT",
        "age": age,
        "income": income,
        "credit_score": credit_score,
        "employment_status": employment_status,
        "years_employed": years_employed,
        "loan_amount": loan_amount,
        "loan_purpose": loan_purpose,
        "existing_debt": existing_debt,
        "debt_to_income_ratio": dti,
        "repayment_history": repayment_history,
        "fraud_flag": fraud_flag,
        "documents_complete": documents_complete,
        "task_type": task_type,
        "expected_risk": "medium",  # dummy (UI mode)
        "expected_decision": "manual_review"
    }

    obs = env._get_observation()

    # Baseline logic (same as your agent)
    if obs.credit_score < 600 or obs.fraud_flag == 1 or obs.debt_to_income_ratio > 0.55:
        action = LoanAction(action_type="underwrite", risk_level="high", decision="reject")

    elif obs.credit_score >= 750 and obs.debt_to_income_ratio < 0.30 and obs.documents_complete == 1:
        action = LoanAction(action_type="underwrite", risk_level="low", decision="approve")

    else:
        action = LoanAction(action_type="underwrite", risk_level="medium", decision="manual_review")

    # Step
    _, reward, _, info = env.step(action)

    # -------------------------------
    # Output Section
    # -------------------------------
    st.header(" AI Decision")

    st.success(f" Risk Level: {action.risk_level}")
    st.info(f" Decision: {action.decision}")

    st.write("###  Reward Score")
    st.write(reward)

    st.write("###  Explanation")
    if action.risk_level == "high":
        st.error("High risk due to low credit score / high debt / fraud flag")
    elif action.risk_level == "medium":
        st.warning("Moderate risk - needs manual review")
    else:
        st.success("Low risk - safe to approve")