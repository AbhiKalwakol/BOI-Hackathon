import pandas as pd
import joblib

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

# ==========================================
# 1. LOAD DATASET
# ==========================================

DATASET_PATH = "data/drebin.csv"

print("Loading dataset...")

df = pd.read_csv(DATASET_PATH)

print(f"Dataset Shape: {df.shape}")

# ==========================================
# 2. PREPARE DATA
# ==========================================

# Convert labels
df["class"] = df["class"].map({
    "B": 0,
    "S": 1
})

# Features and target
X = df.drop("class", axis=1)
y = df["class"]

print(f"Number of Features: {X.shape[1]}")
print(f"Number of Samples : {X.shape[0]}")

# ==========================================
# 3. SAVE FEATURE ORDER
# ==========================================

with open("data/feature_list.txt", "w") as f:
    for feature in X.columns:
        f.write(feature + "\n")

print("Feature list saved.")

# ==========================================
# 4. TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(f"Training Samples: {len(X_train)}")
print(f"Testing Samples : {len(X_test)}")

# ==========================================
# 5. BUILD MODEL
# ==========================================

model = XGBClassifier(
    n_estimators=300,
    max_depth=8,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric="logloss",
    random_state=42,
    n_jobs=-1
)

print("\nTraining model...")

model.fit(X_train, y_train)

print("Training complete.")

# ==========================================
# 6. PREDICTIONS
# ==========================================

y_pred = model.predict(X_test)

y_prob = model.predict_proba(X_test)[:, 1]

# ==========================================
# 7. EVALUATION
# ==========================================

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_prob)

print("\n========== RESULTS ==========")

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
print(f"ROC AUC  : {roc_auc:.4f}")

print("\n========== CONFUSION MATRIX ==========")
print(confusion_matrix(y_test, y_pred))

print("\n========== CLASSIFICATION REPORT ==========")
print(classification_report(y_test, y_pred))

# ==========================================
# 8. SAVE MODEL
# ==========================================

joblib.dump(model, "models/xgboost_model.pkl")

print("\nModel saved:")
print("models/xgboost_model.pkl")

# ==========================================
# 9. SAVE MODEL + FEATURES TOGETHER
# ==========================================

artifacts = {
    "model": model,
    "features": X.columns.tolist()
}

joblib.dump(
    artifacts,
    "models/model_artifacts.pkl"
)

print("Artifacts saved:")
print("models/model_artifacts.pkl")

# ==========================================
# 10. FEATURE IMPORTANCE
# ==========================================

importance = model.feature_importances_

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n========== TOP 20 FEATURES ==========")

print(feature_importance.head(20))

# Optional: Save feature importance
feature_importance.to_csv(
    "data/feature_importance.csv",
    index=False
)

print("\nFeature importance saved:")
print("data/feature_importance.csv")

print("\nTraining pipeline completed successfully.")