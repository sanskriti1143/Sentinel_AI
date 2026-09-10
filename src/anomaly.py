import joblib
import pandas as pd
import os


# =========================
# LOAD ANOMALY MODEL
# =========================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "anomaly_detection_model.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "anomaly_scaler.pkl"
)

anomaly_model = joblib.load(MODEL_PATH)

anomaly_scaler = joblib.load(SCALER_PATH)


# =========================
# ANOMALY DETECTION
# =========================

def detect_anomaly(
    temperature,
    process_temperature,
    rpm,
    torque,
    tool_wear
):

    data = pd.DataFrame([{
        "Air temperature [K]": temperature,
        "Process temperature [K]": process_temperature,
        "Rotational speed [rpm]": rpm,
        "Torque [Nm]": torque,
        "Tool wear [min]": tool_wear
    }])

    # Scale the input
    scaled_data = anomaly_scaler.transform(data)

    # Get anomaly score
    score = anomaly_model.decision_function(scaled_data)[0]

    # Isolation Forest:
    # negative → anomaly
    # positive → normal

    if score < 0:
        prediction = "YES"
    else:
        prediction = "NO"

    return {
        "anomaly_prediction": prediction,
        "anomaly_score": float(score)
    }


print("anomaly.py loaded successfully!")

