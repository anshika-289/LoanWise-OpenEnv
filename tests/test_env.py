from app.env import LoanApprovalEnv
from app.models import LoanAction


def test_env_reset():
    env = LoanApprovalEnv()
    obs = env.reset()
    assert obs.application_id is not None


def test_env_step():
    env = LoanApprovalEnv()
    obs = env.reset()
    action = LoanAction(action_type="underwrite", risk_level="low", decision="approve")
    _, reward, done, info = env.step(action)
    assert isinstance(reward, float)
    assert done is True
    assert "application_id" in info