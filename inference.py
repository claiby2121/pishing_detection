import joblib
from pathlib import Path

MODEL_PATH = Path("../model/phishing_model.pkl")

model = joblib.load(MODEL_PATH)

def predict_email(text: str):
    proba = model.predict_proba([text])[0]
    phishing_index = list(model.classes_).index("Phishing Email")
    phishing_prob = proba[phishing_index]

    prediction = "Phishing Email" if phishing_prob >= 0.5 else "Safe Email"

    return prediction, round(float(phishing_prob * 100), 2)


if __name__ == "__main__":
    sample_email = "Your account has been suspended. Click here to verify."
    result = predict_email(sample_email)
    print(result)
