from app.dataset import load_applications
from app.models import LoanObservation, LoanAction
from app.reward import compute_reward


class LoanApprovalEnv:
    def __init__(self):
        self.applications = load_applications()
        self.index = 0
        self.current = None

    def reset(self):
        self.index = 0
        self.current = self.applications[self.index]
        return self._get_observation()

    def _get_observation(self):
        return LoanObservation(
            application_id=self.current["application_id"],
            age=self.current["age"],
            income=self.current["income"],
            credit_score=self.current["credit_score"],
            employment_status=self.current["employment_status"],
            years_employed=self.current["years_employed"],
            loan_amount=self.current["loan_amount"],
            loan_purpose=self.current["loan_purpose"],
            existing_debt=self.current["existing_debt"],
            debt_to_income_ratio=self.current["debt_to_income_ratio"],
            repayment_history=self.current["repayment_history"],
            fraud_flag=self.current["fraud_flag"],
            documents_complete=self.current["documents_complete"],
            task_type=self.current["task_type"]
        )

    def step(self, action: LoanAction):
        expected_risk = self.current["expected_risk"]
        expected_decision = self.current["expected_decision"]
        task_type = self.current["task_type"]

        reward = compute_reward(
            task_type=task_type,
            predicted_risk=action.risk_level,
            predicted_decision=action.decision,
            expected_risk=expected_risk,
            expected_decision=expected_decision
        )

        info = {
            "expected_risk": expected_risk,
            "expected_decision": expected_decision,
            "application_id": self.current["application_id"]
        }

        done = True
        observation = self._get_observation()
        return observation, reward, done, info

    def state(self):
        return self.current