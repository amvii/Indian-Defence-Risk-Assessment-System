import joblib

model = joblib.load("models/risk_model.pkl")

print("Model loaded successfully!")
import joblib

model = joblib.load("models/risk_model.pkl")
columns = joblib.load("models/model_columns.pkl")

print("Model loaded successfully!")
print("Number of features:", len(columns))
