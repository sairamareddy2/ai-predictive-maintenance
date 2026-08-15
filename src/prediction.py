import os
import joblib
import pandas as pd


# ==========================================
# 1. Locate the project directory
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


# ==========================================
# 2. Load the trained Random Forest model
# ==========================================

model_path = os.path.join(
    BASE_DIR,
    "models",
    "random_forest_model.pkl"
)

model = joblib.load(model_path)


# ==========================================
# 3. Features used by the model
# ==========================================

FEATURES = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
    "Type_H",
    "Type_L",
    "Type_M"
]


# ==========================================
# 4. Machine failure prediction function
# ==========================================

def predict_machine_failure(
    air_temperature,
    process_temperature,
    rotational_speed,
    torque,
    tool_wear,
    machine_type
):

    # Create input data
    input_data = pd.DataFrame([{
        "Air temperature [K]": air_temperature,
        "Process temperature [K]": process_temperature,
        "Rotational speed [rpm]": rotational_speed,
        "Torque [Nm]": torque,
        "Tool wear [min]": tool_wear,

        "Type_H": 1 if machine_type == "H" else 0,
        "Type_L": 1 if machine_type == "L" else 0,
        "Type_M": 1 if machine_type == "M" else 0
    }])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    return prediction, probability


def get_risk_level(probability):

    if probability >= 0.70:
        return "CRITICAL"

    elif probability >= 0.40:
        return "WARNING"

    else:
        return "NORMAL"


def get_maintenance_recommendation(risk_level):

    if risk_level == "CRITICAL":
        return "Immediate maintenance required. Inspect the equipment before continued operation."

    elif risk_level == "WARNING":
        return "Schedule maintenance inspection soon and monitor equipment condition."

    else:
        return "Equipment operating normally. Continue routine monitoring."