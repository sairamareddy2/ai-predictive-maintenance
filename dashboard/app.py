import streamlit as st
import sys
import os
import pandas as pd

# Allow dashboard to access src
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from prediction import (
    predict_machine_failure,
    get_risk_level,
    get_maintenance_recommendation
)


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Predictive Maintenance System",
    page_icon="⚙️",
    layout="wide"
)


# ==========================================
# Title
# ==========================================

st.title("⚙️ Predictive Maintenance System")

st.write(
    "AI-based industrial equipment health monitoring "
    "and failure prediction system."
)


# ==========================================
# Sensor Input Section
# ==========================================

st.header("Equipment Sensor Data")

col1, col2 = st.columns(2)


with col1:

    air_temperature = st.number_input(
        "Air Temperature [K]",
        min_value=295.0,
        max_value=305.0,
        value=300.0,
        step=0.1
    )

    process_temperature = st.number_input(
        "Process Temperature [K]",
        min_value=305.0,
        max_value=315.0,
        value=310.0,
        step=0.1
    )

    rotational_speed = st.number_input(
        "Rotational Speed [rpm]",
        min_value=1000,
        max_value=3000,
        value=1500,
        step=10
    )


with col2:

    torque = st.number_input(
        "Torque [Nm]",
        min_value=0.0,
        max_value=80.0,
        value=40.0,
        step=0.1
    )

    tool_wear = st.number_input(
        "Tool Wear [min]",
        min_value=0,
        max_value=300,
        value=100,
        step=1
    )

    machine_type = st.selectbox(
        "Machine Type",
        ["L", "M", "H"]
    )


# ==========================================
# Prediction Button
# ==========================================

if st.button("🔍 Predict Equipment Health"):

    prediction, probability = predict_machine_failure(
        air_temperature,
        process_temperature,
        rotational_speed,
        torque,
        tool_wear,
        machine_type
    )

    risk_level = get_risk_level(probability)

    recommendation = get_maintenance_recommendation(
        risk_level
    )


    # ==========================================
# Results
# ==========================================

st.header("Prediction Results")

result_col1, result_col2, result_col3 = st.columns(3)

with result_col1:
    st.metric(
        "Failure Probability",
        f"{probability * 100:.1f}%"
    )

with result_col2:
    st.metric(
        "Prediction",
        "FAILURE" if prediction == 1 else "NORMAL"
    )

with result_col3:
    st.metric(
        "Risk Level",
        risk_level
    )


# ==========================================
# Health Status
# ==========================================

st.subheader("Equipment Health")

if risk_level == "CRITICAL":

    st.error("🔴 CRITICAL — Immediate maintenance required.")

elif risk_level == "WARNING":

    st.warning("🟡 WARNING — Maintenance inspection recommended.")

else:

    st.success("🟢 NORMAL — Equipment operating normally.")


# ==========================================
# Failure Probability
# ==========================================

st.subheader("Failure Probability")

st.progress(
    float(probability)
)

st.write(
    f"Current predicted failure probability: "
    f"**{probability * 100:.1f}%**"
)


# ==========================================
# Maintenance Recommendation
# ==========================================

st.subheader("Maintenance Recommendation")

if risk_level == "CRITICAL":

    st.error(recommendation)

elif risk_level == "WARNING":

    st.warning(recommendation)

else:

    st.success(recommendation)


# ==========================================
# Sensor Summary
# ==========================================

st.subheader("Current Sensor Readings")

sensor_data = pd.DataFrame({
    "Parameter": [
        "Air Temperature [K]",
        "Process Temperature [K]",
        "Rotational Speed [rpm]",
        "Torque [Nm]",
        "Tool Wear [min]",
        "Machine Type"
    ],
    "Value": [
        air_temperature,
        process_temperature,
        rotational_speed,
        torque,
        tool_wear,
        machine_type
    ]
})

st.dataframe(
    sensor_data,
    use_container_width=True,
    hide_index=True
)