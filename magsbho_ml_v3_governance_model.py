# magsbho_ml_v3_governance_model.py

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    recall_score,
    precision_score,
    confusion_matrix,
    classification_report,
)

# --------------------------------------------------------
# MAGSBHO ML v3
# Multi-class governance model for safety-critical systems
# --------------------------------------------------------

label_names = {
    0: "ROUTINE_SUPPORT",
    1: "SUPPORT_AND_MONITOR",
    2: "ESCALATE_TO_HUMAN",
}

# --------------------------------------------------------
# Simulated governance dataset
# --------------------------------------------------------

data = [
    [2, 1, 2, 0, 0], [3, 2, 3, 0, 0], [4, 2, 4, 0, 0],
    [5, 3, 4, 0, 1], [5, 4, 5, 0, 1], [6, 4, 5, 1, 1],
    [6, 5, 6, 1, 1], [7, 5, 6, 1, 1], [7, 6, 7, 1, 2],
    [8, 6, 7, 1, 2], [8, 7, 8, 1, 2], [9, 8, 9, 1, 2],
    [3, 1, 4, 0, 0], [4, 3, 5, 0, 1], [5, 5, 6, 1, 1],
    [6, 6, 7, 1, 2], [7, 7, 8, 1, 2], [2, 2, 2, 0, 0],
    [3, 3, 3, 0, 0], [4, 4, 4, 0, 1], [5, 5, 5, 1, 1],
    [6, 6, 6, 1, 1], [7, 7, 7, 1, 2], [8, 8, 8, 1, 2],
    [9, 9, 9, 1, 2], [4, 1, 6, 0, 1], [3, 6, 3, 0, 1],
    [6, 2, 7, 1, 1], [2, 7, 2, 0, 1], [8, 3, 8, 1, 2],
    [5, 6, 5, 1, 1], [6, 7, 6, 1, 2], [4, 5, 4, 0, 1],
    [3, 4, 3, 0, 0], [7, 4, 8, 1, 2], [5, 2, 5, 0, 1],
    [6, 3, 6, 1, 1], [8, 5, 8, 1, 2], [4, 6, 4, 1, 1],
    [2, 3, 2, 0, 0],
]

df = pd.DataFrame(
    data,
    columns=["stress", "conflict", "cognitive_load", "repeated_issue", "action"]
)

X = df[["stress", "conflict", "cognitive_load", "repeated_issue"]]
y = df["action"]

# --------------------------------------------------------
# Train/Test Split
# --------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

# --------------------------------------------------------
# Models
# --------------------------------------------------------

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42),
}

results = []

print("\nMAGSBHO ML v3 - GOVERNANCE MODEL")
print("=" * 60)

# --------------------------------------------------------
# Training Loop
# --------------------------------------------------------

for name, model in models.items():
    model.fit(X_train, y_train)

    # 🔬 CROSS-VALIDATION (KEY UPGRADE)
    scores = cross_val_score(model, X, y, cv=5)
    print(f"\n{name} Cross-validation accuracy: {scores.mean():.3f}")

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    rec_escalate = recall_score(
        y_test, y_pred, labels=[2], average="macro", zero_division=0
    )
    prec_escalate = precision_score(
        y_test, y_pred, labels=[2], average="macro", zero_division=0
    )

    results.append({
        "Model": name,
        "Accuracy": round(acc, 3),
        "Recall (Escalate)": round(rec_escalate, 3),
        "Precision (Escalate)": round(prec_escalate, 3),
    })

    print(f"\n{name}")
    print("-" * 60)
    print(f"Accuracy: {acc:.3f}")
    print(f"Recall (Escalate): {rec_escalate:.3f}")
    print(f"Precision (Escalate): {prec_escalate:.3f}")

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(classification_report(
        y_test,
        y_pred,
        target_names=[
            "ROUTINE_SUPPORT",
            "SUPPORT_AND_MONITOR",
            "ESCALATE_TO_HUMAN",
        ],
        zero_division=0
    ))

# --------------------------------------------------------
# Summary
# --------------------------------------------------------

results_df = pd.DataFrame(results)

print("\nSUMMARY TABLE")
print("=" * 60)
print(results_df.to_string(index=False))

# --------------------------------------------------------
# Best Model Selection
# --------------------------------------------------------

best_model_row = sorted(
    results,
    key=lambda r: (r["Recall (Escalate)"], r["Accuracy"]),
    reverse=True
)[0]

print("\nBEST SAFETY-ALIGNED MODEL")
print("=" * 60)
print(
    f"{best_model_row['Model']} | "
    f"Accuracy: {best_model_row['Accuracy']:.3f} | "
    f"Recall (Escalate): {best_model_row['Recall (Escalate)']:.3f} | "
    f"Precision (Escalate): {best_model_row['Precision (Escalate)']:.3f}"
)

# --------------------------------------------------------
# New Scenario Predictions
# --------------------------------------------------------

new_scenarios = pd.DataFrame([
    {"stress": 9, "conflict": 8, "cognitive_load": 9, "repeated_issue": 1},
    {"stress": 3, "conflict": 2, "cognitive_load": 3, "repeated_issue": 0},
    {"stress": 6, "conflict": 5, "cognitive_load": 6, "repeated_issue": 1},
    {"stress": 4, "conflict": 4, "cognitive_load": 4, "repeated_issue": 0},
])

if best_model_row["Model"] == "Logistic Regression":
    best_model = LogisticRegression(max_iter=1000)
else:
    best_model = DecisionTreeClassifier(max_depth=4, random_state=42)

best_model.fit(X_train, y_train)
new_preds = best_model.predict(new_scenarios)

print("\nNEW SCENARIO PREDICTIONS")
print("=" * 60)

for i, row in new_scenarios.iterrows():
    pred = new_preds[i]
    print(f"\nScenario {i+1}")
    print(
        f"Inputs: stress={row['stress']}, conflict={row['conflict']}, "
        f"cognitive_load={row['cognitive_load']}, repeated_issue={row['repeated_issue']}"
    )
    print(f"Predicted action: {label_names[pred]}")

# --------------------------------------------------------
# Save Results
# --------------------------------------------------------

results_df.to_csv("magsbho_ml_v3_results.csv", index=False)
print("\nSaved results to magsbho_ml_v3_results.csv")

input("\nPress Enter to close...")