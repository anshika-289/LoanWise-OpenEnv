# LoanWise-OpenEnv

LoanWise-OpenEnv is a realistic loan underwriting environment for evaluating AI agents on financial decision-making tasks.

## Problem
Banks must evaluate loan applications and balance risk vs growth.

## Tasks
1. Risk classification
2. Loan decision
3. Full underwriting workflow

## Observation Space
Includes:
- income
- credit score
- debt-to-income ratio
- employment status
- repayment history

## Action Space
Agent outputs:
- risk_level (low/medium/high)
- decision (approve/reject/manual_review)
- reason (explainability)

## Reward
- correct risk: +0.3
- correct decision: +0.4
- correct reason: +0.1
- wrong approval: -1.0

## Graders
- Risk grader
- Decision grader
- Workflow grader

## Run Locally
pip install -r requirements.txt
python scripts/demo.py

## Docker
docker build -t loanwise .
docker run loanwise

## Why this project?
Simulates real-world loan underwriting used in banks and fintech.

Includes explainable AI + risk scoring.