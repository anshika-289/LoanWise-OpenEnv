from app.env import LoanApprovalEnv
from app.models import LoanAction


def baseline_policy(obs):
    if obs.credit_score < 600 or obs.fraud_flag == 1 or obs.debt_to_income_ratio > 0.55:
        return LoanAction(action_type="underwrite", risk_level="high", decision="reject")

    if obs.credit_score >= 750 and obs.debt_to_income_ratio < 0.30 and obs.documents_complete == 1:
        return LoanAction(action_type="underwrite", risk_level="low", decision="approve")

    return LoanAction(action_type="underwrite", risk_level="medium", decision="manual_review")


def main():
    env = LoanApprovalEnv()
    total_reward = 0.0

    for i, case in enumerate(env.applications):
        env.current = case
        obs = env._get_observation()
        action = baseline_policy(obs)
        _, reward, _, info = env.step(action)
        total_reward += reward
        print(f"{i+1}. {info['application_id']} -> reward={reward}")

    print(f"\nTotal reward: {total_reward}")


if __name__ == "__main__":
    main()