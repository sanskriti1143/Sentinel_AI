
def explain_prediction(
    temperature,
    process_temperature,
    rpm,
    torque,
    tool_wear,
    machine_type
):

    factors = {
        "Torque": torque,
        "Tool Wear": tool_wear,
        "RPM": rpm,
        "Temperature": temperature,
        "Process Temperature": process_temperature
    }

    # Sort factors by their values
    sorted_factors = sorted(
        factors.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # Return top 3
    return [factor[0] for factor in sorted_factors[:3]]


print("explainability.py loaded successfully!")
