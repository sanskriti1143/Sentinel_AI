
from src.prediction import predict_failure
from src.anomaly import detect_anomaly
from src.explainability import explain_prediction


def analyze_machine(
    temperature,
    process_temperature,
    rpm,
    torque,
    tool_wear,
    machine_type
):

    # Failure prediction
    failure = predict_failure(
        temperature,
        process_temperature,
        rpm,
        torque,
        tool_wear,
        machine_type
    )

    # Anomaly detection
    anomaly = detect_anomaly(
        temperature,
        process_temperature,
        rpm,
        torque,
        tool_wear
    )

    # Risk factors
    risk_factors = explain_prediction(
        temperature,
        process_temperature,
        rpm,
        torque,
        tool_wear,
        machine_type
    )

    return {
        "failure_probability": failure["failure_probability"],
        "failure_prediction": failure["failure_prediction"],
        "anomaly_prediction": anomaly["anomaly_prediction"],
        "anomaly_score": anomaly["anomaly_score"],
        "top_risk_factors": risk_factors
    }


print("sentinel_engine.py loaded successfully!")
