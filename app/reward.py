def compute_reward(task_type, predicted_risk, predicted_decision, expected_risk, expected_decision):
    reward = 0.0

    if task_type == "risk":
        if predicted_risk == expected_risk:
            reward += 1.0

    elif task_type == "decision":
        if predicted_decision == expected_decision:
            reward += 1.0
        elif predicted_decision == "approve" and expected_decision == "reject":
            reward -= 1.0
        else:
            reward -= 0.5

    elif task_type == "workflow":
        if predicted_risk == expected_risk:
            reward += 0.3
        if predicted_decision == expected_decision:
            reward += 0.5
        if predicted_decision == "approve" and expected_decision == "reject":
            reward -= 1.0

    return reward