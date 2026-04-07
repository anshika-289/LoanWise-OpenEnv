import random
from pydantic import BaseModel
from typing import Optional


class LoanObservation(BaseModel):
    application_id: str
    credit_score: int
    debt_to_income_ratio: float
    fraud_flag: int


class LoanAction(BaseModel):
    risk_level: str
    decision: str


class LoanStepResult(BaseModel):
    observation: LoanObservation
    reward: float
    done: bool


class LoanEnv:

    def __init__(self):
        self.current = None

    async def reset(self):
        self.current = {
            "application_id": "A001",
            "credit_score": random.randint(500, 800),
            "debt_to_income_ratio": round(random.uniform(0.1, 0.7), 2),
            "fraud_flag": random.choice([0, 1])
        }

        return LoanStepResult(
            observation=LoanObservation(**self.current),
            reward=0.0,
            done=False
        )

    async def step(self, action: LoanAction):

        score = 0.0

        if self.current["credit_score"] < 600 or self.current["fraud_flag"] == 1:
            correct = "reject"
        elif self.current["credit_score"] > 750:
            correct = "approve"
        else:
            correct = "manual_review"

        if action.decision == correct:
            score = 1.0
        else:
            score = 0.0

        return LoanStepResult(
            observation=LoanObservation(**self.current),
            reward=score,
            done=True
        )

    async def close(self):
        pass