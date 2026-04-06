def risk_grader(predicted, expected):
    return 1.0 if predicted == expected else 0.0


def decision_grader(predicted, expected):
    if predicted == expected:
        return 1.0
    if predicted == "manual_review":
        return 0.7
    return 0.0


def workflow_grader(pred_risk, pred_decision, exp_risk, exp_decision):
    score = 0.0

    if pred_risk == exp_risk:
        score += 0.3

    if pred_decision == exp_decision:
        score += 0.5

    if pred_decision == "approve" and exp_decision == "reject":
        score -= 1.0

    return score

