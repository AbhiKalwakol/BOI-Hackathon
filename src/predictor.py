import joblib
import numpy as np

artifacts = joblib.load("models/model_artifacts.pkl")

model = artifacts["model"]
feature_names = artifacts["features"]


def predict(feature_vector):

    feature_vector = np.array(feature_vector).reshape(1, -1)

    prediction = model.predict(feature_vector)[0]

    probabilities = model.predict_proba(feature_vector)[0]

    confidence = max(probabilities)

    return prediction, confidence, probabilities