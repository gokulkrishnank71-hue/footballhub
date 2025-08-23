import pickle
import numpy as np
import pandas as pd

# 🔹 Load trained model and label encoder
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# Feature names used during training
feature_names = [
    'HomeShots', 'AwayShots', 'HomeShotsOnTarget', 'AwayShotsOnTarget',
    'HomeCorners', 'AwayCorners', 'HomeFouls', 'AwayFouls',
    'HomeYellowCards', 'AwayYellowCards', 'HomeRedCards', 'AwayRedCards'
]

# Example match stats (⚽ update values)
match_stats = pd.DataFrame([[15, 10, 7, 4, 6, 3, 12, 14, 2, 3, 0, 0]],
                           columns=feature_names)

# 🔹 Predict result
prediction = model.predict(match_stats)
predicted_result = label_encoder.inverse_transform(prediction)[0]

print("📊 Predicted Match Result:", predicted_result)
