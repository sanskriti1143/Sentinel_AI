
import streamlit as st
from datetime import datetime

from src.sentinel_engine import analyze_machine


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Sentinel AI",
    page_icon="🛡️",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* Main page */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Header */
    .title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0;
    }

    .subtitle {
        font-size: 18px;
        color: #777;
        margin-bottom: 25px;
    }

    /* Cards */
    .card {
        padding: 22px;
        border-radius: 15px;
        border: 1px solid #dddddd;
        background: #fafafa;
        margin-bottom: 15px;
    }

    .card-title {
        font-size: 16px;
        color: #777;
        margin-bottom: 5px;
    }

    .card-value {
        font-size: 30px;
        font-weight: 750;
    }

    /* Risk */
    .risk-high {
        padding: 25px;
        border-radius: 15px;
        background-color: #ffe5e5;
        border: 1px solid #ffb3b3;
        text-align: center;
    }

    .risk-low {
        padding: 25px;
        border-radius: 15px;
        background-color: #e8f7ed;
        border: 1px solid #b7e4c7;
        text-align: center;
    }

    .risk-title {
        font-size: 16px;
        color: #666;
    }

    .risk-value {
        font-size: 36px;
        font-weight: 800;
    }

    /* Factors */
    .factor {
        padding: 12px 15px;
        margin: 7px 0;
        border-radius: 9px;
        background-color: #f2f2f2;
        font-weight: 600;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #888;
        margin-top: 40px;
        font-size: 13px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">🛡️ Sentinel AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predictive Maintenance Intelligence System'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# MACHINE INFORMATION
# =========================================================

st.markdown("### 🏭 Machine Information")

machine_id = st.text_input(
    "Machine ID",
    value="A102"
)


# =========================================================
# SENSOR INPUTS
# =========================================================

st.markdown("### ⚙️ Sensor Parameters")

col1, col2, col3 = st.columns(3)

with col1:

    temperature = st.number_input(
        "Air Temperature [K]",
        value=301.0
    )

    process_temperature = st.number_input(
        "Process Temperature [K]",
        value=311.0
    )


with col2:

    rpm = st.number_input(
        "Rotational Speed [rpm]",
        value=1500
    )

    torque = st.number_input(
        "Torque [Nm]",
        value=50.0
    )


with col3:

    tool_wear = st.number_input(
        "Tool Wear [min]",
        value=180.0
    )

    machine_type = st.selectbox(
        "Machine Type",
        ["L", "M", "H"]
    )


st.write("")


# =========================================================
# ANALYZE BUTTON
# =========================================================

analyze = st.button(
    "🔍 ANALYZE MACHINE",
    use_container_width=True
)


# =========================================================
# ANALYSIS
# =========================================================

if analyze:

    result = analyze_machine(
        temperature,
        process_temperature,
        rpm,
        torque,
        tool_wear,
        machine_type
    )

    failure_probability = (
        result["failure_probability"] * 100
    )

    failure_prediction = result["failure_prediction"]

    anomaly_prediction = result["anomaly_prediction"]

    anomaly_score = result["anomaly_score"]

    risk_factors = result["top_risk_factors"]


    st.divider()


    # =====================================================
    # MACHINE STATUS
    # =====================================================

    st.markdown("### 🚦 Machine Status")

    if failure_prediction == "HIGH RISK":

        st.markdown(
            f"""
            <div class="risk-high">
                <div class="risk-title">
                    MACHINE {machine_id}
                </div>
                <div class="risk-value">
                    🚨 HIGH RISK
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="risk-low">
                <div class="risk-title">
                    MACHINE {machine_id}
                </div>
                <div class="risk-value">
                    ✅ LOW RISK
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.write("")


    # =====================================================
    # METRICS
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Failure Probability",
            f"{failure_probability:.1f}%"
        )


    with col2:

        st.metric(
            "Anomaly",
            anomaly_prediction
        )


    with col3:

        st.metric(
            "Anomaly Score",
            f"{anomaly_score:.4f}"
        )


    # =====================================================
    # FAILURE PROBABILITY
    # =====================================================

    st.markdown("### 📊 Failure Probability")

    st.progress(
        min(max(failure_probability / 100, 0.0), 1.0)
    )

    st.caption(
        f"Model confidence: {failure_probability:.1f}% probability of machine failure"
    )


    # =====================================================
    # SENSOR OVERVIEW
    # =====================================================

    st.markdown("### 📡 Sensor Overview")

    sensor_col1, sensor_col2, sensor_col3, sensor_col4, sensor_col5 = st.columns(5)

    with sensor_col1:
        st.metric("Temperature", f"{temperature:.1f} K")

    with sensor_col2:
        st.metric("Process Temp", f"{process_temperature:.1f} K")

    with sensor_col3:
        st.metric("RPM", f"{rpm}")

    with sensor_col4:
        st.metric("Torque", f"{torque:.1f} Nm")

    with sensor_col5:
        st.metric("Tool Wear", f"{tool_wear:.0f} min")


    # =====================================================
    # RISK FACTORS
    # =====================================================

    st.markdown("### ⚠️ Top Risk Factors")

    factor_col1, factor_col2 = st.columns([2, 1])

    with factor_col1:

        for i, factor in enumerate(risk_factors, 1):

            st.markdown(
                f'<div class="factor">{i}. {factor}</div>',
                unsafe_allow_html=True
            )

    with factor_col2:

        st.info(
            "These features were identified by the "
            "Sentinel AI explainability module as the "
            "top factors associated with the prediction."
        )


    # =====================================================
    # FINAL ALERT
    # =====================================================

    st.markdown("### 🔔 Recommendation")

    if failure_prediction == "HIGH RISK":

        st.error(
            "Immediate inspection recommended. "
            "The machine has a high predicted probability "
            "of failure."
        )

    elif anomaly_prediction == "YES":

        st.warning(
            "An unusual machine condition was detected. "
            "Consider inspecting the machine before continued operation."
        )

    else:

        st.success(
            "Machine operating within expected conditions. "
            "No immediate action required."
        )


    # =====================================================
    # TIMESTAMP
    # =====================================================

    st.caption(
        "Analysis performed: "
        + datetime.now().strftime("%d %B %Y, %H:%M:%S")
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer">'
    'Sentinel AI • Predictive Maintenance System'
    '</div>',
    unsafe_allow_html=True
)
