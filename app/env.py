from app.dataset import load_applications
from app.models import LoanObservation, LoanAction
from app.reward import compute_reward


class LoanApprovalEnv:
    def __init__(self):
        self.applications = load_applications()
        self.current = None

    def reset(self):
        self.current = self.applications[0]
        return self._get_observation()

    def _get_observation(self):
        return LoanObservation(**self.current)

    def step(self, action: LoanAction):
        reward = compute_reward(
            task_type=self.current["task_type"],
            predicted_risk=action.risk_level,
            predicted_decision=action.decision,
            expected_risk=self.current["expected_risk"],
            expected_decision=self.current["expected_decision"]
        )

        return self._get_observation(), reward, True, {"id": self.current["application_id"]}

    def state(self):
        return self.current