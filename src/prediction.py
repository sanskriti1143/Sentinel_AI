import joblib
import pandas as pd
import os


# =========================
# LOAD SAVED MODEL
# =========================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "failure_prediction_model.pkl"
)

THRESHOLD_PATH = os.path.join(
    BASE_DIR,
    "models",
    "best_threshold.pkl"
)

model = joblib.load(MODEL_PATH)

threshold = joblib.load(THRESHOLD_PATH)


# =========================
# FAILURE PREDICTION
# =========================

def predict_failure(
    temperature,
    process_temperature,
    rpm,
    torque,
    tool_wear,
    machine_type
):

    # Create input dataframe
    data = pd.DataFrame([{
        "Air temperature [K]": temperature,
        "Process temperature [K]": process_temperature,
        "Rotational speed [rpm]": rpm,
        "Torque [Nm]": torque,
        "Tool wear [min]": tool_wear,
        "Type": machine_type
    }])

    # The saved Pipeline already contains preprocessing.
    # Therefore, DO NOT use pd.get_dummies() here.

    probability = model.predict_proba(data)[0][1]

    # Apply saved threshold
    if probability >= threshold:
        prediction = "HIGH RISK"
    else:
        prediction = "LOW RISK"

    return {
        "failure_probability": float(probability),
        "failure_prediction": prediction
    }


print("prediction.py loaded successfully!")

