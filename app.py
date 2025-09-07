import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
df = pd.read_csv("diabetes.csv")

# Split into features and target
X = df.drop(columns=["Diabetic"])
y = df["Diabetic"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define base learners
base_learners = [
    ('knn', KNeighborsClassifier(n_neighbors=5)),
    ('dt', DecisionTreeClassifier(random_state=42)),
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42))
]

# Define meta-learner (usually Logistic Regression)
meta_learner = LogisticRegression()

# Build Stacking Classifier
stack_clf = StackingClassifier(estimators=base_learners, final_estimator=meta_learner, cv=5)

# Train Stacking Classifier
stack_clf.fit(X_train_scaled, y_train)

# Predict and evaluate
y_pred = stack_clf.predict(X_test_scaled)

print("Stacking Classifier Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(stack_clf, "stacking_model.pkl")

# Save the scaler
joblib.dump(scaler, "scaler.pkl")

print("Model and scaler saved successfully.")