from app.env import LoanApprovalEnv
from app.models import LoanAction

env = LoanApprovalEnv()
obs = env.reset()

print("Initial Observation:")
print(obs.model_dump())

action = LoanAction(
    action_type="underwrite",
    risk_level="low",
    decision="approve"
)

next_obs, reward, done, info = env.step(action)

print("\nReward:", reward)