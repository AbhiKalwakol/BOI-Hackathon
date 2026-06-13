from extract import extract_features
from predictor import predict
from report_generator import (generate_report)
from risk_score import (
    generate_risk_score,
    label_risk
)


def main():

    print("=" * 50)
    print("BOI Malware Detection System")
    print("=" * 50)

    print(
        "\nWaiting for APK feature extraction..."
    )

    # Temporary dummy vector

    apk_path = "uploads/sample.apk"

    feature_vector = extract_features(
        apk_path
    )
    print(
        f"Feature Vector Length: "
        f"{len(feature_vector)}"
    )

    print(
        f"Detected Features: "
        f"{sum(feature_vector)}"
    )

    prediction, confidence, probs = predict(
        feature_vector
    )

    risk_score = generate_risk_score(
        confidence
    )

    risk_level = label_risk(
        risk_score
    )

    print("\nPrediction")

    if prediction == 1:
        print("Malware")
    else:
        print("Benign")

    print(
        f"Confidence : {confidence:.4f}"
    )

    print(
        f"Risk Score : {risk_score}"
    )

    print(
        f"Risk Level : {risk_level}"
    )
    with open("data/feature_list.txt") as f:
        names = [line.strip() for line in f]


    print(f"Detected Features: {sum(feature_vector)} / 215")

    for i, value in enumerate(feature_vector):

        if value == 1:
            print(names[i])

    detected_features = []
    for i, value in enumerate(feature_vector):
        if value == 1:
            detected_features.append(
                feature_names[i]
            )
    report = generate_report(
        prediction,
        confidence,
        detected_features
    )

    print(report)
    with open(
            "reports/report.txt",
            "w",
            encoding="utf-8"
    ) as f:
        f.write(report)

if __name__ == "__main__":
    main()