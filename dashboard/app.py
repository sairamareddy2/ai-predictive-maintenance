import streamlit as st
import sys
import os
import pandas as pd


# =========================================================
# PROJECT PATH
# =========================================================

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


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Predictive Maintenance",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 600;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    .normal-box {
        padding: 18px;
        border-radius: 10px;
        border: 1px solid #2e7d32;
        text-align: center;
        font-size: 20px;
        font-weight: 600;
    }

    .warning-box {
        padding: 18px;
        border-radius: 10px;
        border: 1px solid #f9a825;
        text-align: center;
        font-size: 20px;
        font-weight: 600;
    }

    .critical-box {
        padding: 18px;
        border-radius: 10px;
        border: 1px solid #c62828;
        text-align: center;
        font-size: 20px;
        font-weight: 600;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        padding: 15px;
        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">⚙️ AI Predictive Maintenance System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Industrial equipment health monitoring and failure prediction '
    'using Machine Learning.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# SIDEBAR - MODEL INFORMATION
# =========================================================

with st.sidebar:

    st.header("🤖 Model Information")

    st.write("**Model:** Random Forest")
    st.write("**Model Type:** Classification")
    st.write("**Number of Trees:** 200")
    st.write("**Input Features:** 8")
    st.write("**Training Records:** 8,000")
    st.write("**Testing Records:** 2,000")

    st.divider()

    st.subheader("📊 Model Performance")

    st.metric(
        "Test Accuracy",
        "97.95%"
    )

    st.metric(
        "Failure Recall",
        "64.71%"
    )

    st.divider()

    st.caption(
        "Prototype developed for AI-based predictive maintenance."
    )


# =========================================================
# EQUIPMENT INPUT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">🔧 Equipment Sensor Inputs</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter the current operating conditions of the equipment."
)

col1, col2 = st.columns(2)


# ---------------------------------------------------------
# LEFT COLUMN
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# RIGHT COLUMN
# ---------------------------------------------------------

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


st.write("")


# =========================================================
# PREDICTION BUTTON
# =========================================================

predict_button = st.button(
    "🔍 Analyze Equipment Health",
    use_container_width=True,
    type="primary"
)


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

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


    st.divider()


    # =====================================================
    # RESULTS HEADER
    # =====================================================

    st.markdown(
        '<div class="section-title">📊 Equipment Health Assessment</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # RESULT METRICS
    # =====================================================

    result_col1, result_col2, result_col3 = st.columns(3)


    with result_col1:

        st.metric(
            "Failure Probability",
            f"{probability * 100:.1f}%"
        )


    with result_col2:

        prediction_text = (
            "FAILURE"
            if prediction == 1
            else "NORMAL"
        )

        st.metric(
            "Prediction",
            prediction_text
        )


    with result_col3:

        st.metric(
            "Risk Level",
            risk_level
        )


    # =====================================================
    # PROBABILITY BAR
    # =====================================================

    st.subheader("Failure Probability")

    st.progress(
        min(float(probability), 1.0)
    )

    st.write(
        f"Predicted probability of equipment failure: "
        f"**{probability * 100:.1f}%**"
    )


    # =====================================================
    # HEALTH STATUS
    # =====================================================

    st.subheader("Equipment Health Status")


    if risk_level == "CRITICAL":

        st.markdown(
            """
            <div class="critical-box">
            🔴 CRITICAL<br>
            Immediate attention required
            </div>
            """,
            unsafe_allow_html=True
        )

        st.error(
            recommendation
        )


    elif risk_level == "WARNING":

        st.markdown(
            """
            <div class="warning-box">
            🟡 WARNING<br>
            Increased risk detected
            </div>
            """,
            unsafe_allow_html=True
        )

        st.warning(
            recommendation
        )


    else:

        st.markdown(
            """
            <div class="normal-box">
            🟢 NORMAL<br>
            Equipment operating normally
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success(
            recommendation
        )


    # =====================================================
    # SENSOR SUMMARY
    # =====================================================

    st.subheader("📋 Current Sensor Readings")


    sensor_data = pd.DataFrame(
        {
            "Parameter": [
                "Air Temperature",
                "Process Temperature",
                "Rotational Speed",
                "Torque",
                "Tool Wear",
                "Machine Type"
            ],

            "Value": [
                f"{air_temperature:.1f} K",
                f"{process_temperature:.1f} K",
                f"{rotational_speed} rpm",
                f"{torque:.1f} Nm",
                f"{tool_wear} min",
                machine_type
            ]
        }
    )


    st.dataframe(
        sensor_data,
        use_container_width=True,
        hide_index=True
    )


    # =====================================================
    # MAINTENANCE ACTION
    # =====================================================

    st.subheader("🔧 Recommended Maintenance Action")

    if risk_level == "CRITICAL":

        st.error(
            "Immediate maintenance required. "
            "Inspect the equipment before continued operation."
        )

    elif risk_level == "WARNING":

        st.warning(
            "Schedule a maintenance inspection soon "
            "and continue monitoring equipment condition."
        )

    else:

        st.success(
            "No immediate maintenance action required. "
            "Continue routine monitoring."
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    '<div class="footer">'
    'AI Predictive Maintenance System | '
    'Random Forest Machine Learning Model | '
    'Internship Project Prototype'
    '</div>',
    unsafe_allow_html=True
)