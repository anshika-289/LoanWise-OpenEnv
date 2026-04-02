from pydantic import BaseModel
from typing import Optional, Literal, Dict, Any


class LoanObservation(BaseModel):
    application_id: str
    age: int
    income: float
    credit_score: int
    employment_status: str
    years_employed: int
    loan_amount: float
    loan_purpose: str
    existing_debt: float
    debt_to_income_ratio: float
    repayment_history: str
    fraud_flag: int
    documents_complete: int
    task_type: str


class LoanAction(BaseModel):
    action_type: Literal["predict_risk", "decide", "underwrite"]
    risk_level: Optional[Literal["low", "medium", "high"]] = None
    decision: Optional[Literal["approve", "reject", "manual_review"]] = None


class StepResult(BaseModel):
    observation: LoanObservation
    reward: float
    done: bool
    info: Dict[str, Any]