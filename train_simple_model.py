import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data
df = pd.read_csv("data/2000-25-data.csv")

# Keep only relevant columns
df = df[['HomeTeam', 'AwayTeam', 'FullTimeResult']]
df.rename(columns={'FullTimeResult': 'Result'}, inplace=True)

# Encode categorical values (teams + result)
from sklearn.preprocessing import LabelEncoder
home_encoder = LabelEncoder()
away_encoder = LabelEncoder()
result_encoder = LabelEncoder()

df['HomeTeam'] = home_encoder.fit_transform(df['HomeTeam'])
df['AwayTeam'] = away_encoder.fit_transform(df['AwayTeam'])
df['Result'] = result_encoder.fit_transform(df['Result'])

# Features and target
X = df[['HomeTeam', 'AwayTeam']]
y = df['Result']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model + encoders
with open("simple_model.pkl", "wb") as f:
    pickle.dump({
        "model": model,
        "home_encoder": home_encoder,
        "away_encoder": away_encoder,
        "result_encoder": result_encoder
    }, f)

print("✅ Simple model trained and saved as simple_model.pkl")
