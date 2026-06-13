def generate_risk_score(confidence):

    return round(confidence * 100, 2)


def label_risk(score):

    if score >= 90:
        return "Critical"

    elif score >= 70:
        return "High"

    elif score >= 40:
        return "Medium"

    return "Low"