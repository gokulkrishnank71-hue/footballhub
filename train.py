import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("2000-25-data.csv")
print("✅ Data loaded successfully!")
print("Columns in dataset:", df.columns)

# Check if target column exists
if "FullTimeResult" not in df.columns:
    raise ValueError("❌ Could not find target column 'FullTimeResult' in dataset!")

# Features and target
X = df[[
    "HomeShots", "AwayShots", "HomeShotsOnTarget", "AwayShotsOnTarget",
    "HomeCorners", "AwayCorners", "HomeFouls", "AwayFouls",
    "HomeYellowCards", "AwayYellowCards", "HomeRedCards", "AwayRedCards"
]]

y = df["FullTimeResult"]

# Encode target labels (H=Home win, A=Away win, D=Draw)
le = LabelEncoder()
y = le.fit_transform(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Accuracy
print("✅ Model trained!")
print("🔹 Training Accuracy:", model.score(X_train, y_train))
print("🔹 Test Accuracy:", model.score(X_test, y_test))

# Cross-validation
scores = cross_val_score(model, X, y, cv=5)
print("🔄 Cross-Validation Accuracy:", scores.mean())

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save label encoder
with open("label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

print("✅ Model & Encoder saved as model.pkl and label_encoder.pkl")
