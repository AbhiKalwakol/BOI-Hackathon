def generate_report(prediction,confidence,detected_features):

    report = []

    if prediction == 1:
        report.append(
            "APK classified as MALWARE."
        )
    else:
        report.append(
            "APK classified as BENIGN."
        )

    report.append(
        f"Confidence: {confidence:.2%}"
    )

    report.append(
        "\nSuspicious Indicators:"
    )

    for feature in detected_features[:15]:
        report.append(
            f"- {feature}"
        )

    return "\n".join(report)