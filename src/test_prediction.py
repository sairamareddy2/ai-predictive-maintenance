from prediction import (
    predict_machine_failure,
    get_risk_level,
    get_maintenance_recommendation
)


def test_machine(
    air_temperature,
    process_temperature,
    rotational_speed,
    torque,
    tool_wear,
    machine_type
):

    prediction, probability = predict_machine_failure(
        air_temperature,
        process_temperature,
        rotational_speed,
        torque,
        tool_wear,
        machine_type
    )

    risk = get_risk_level(probability)

    recommendation = get_maintenance_recommendation(risk)

    print("\n-----------------------------")
    print("Machine Type:", machine_type)
    print("Prediction:", prediction)
    print("Failure Probability:", probability * 100, "%")
    print("Risk Level:", risk)
    print("Recommendation:", recommendation)


# Test 1 - Normal equipment
test_machine(
    300.0,
    310.0,
    1500,
    40.0,
    50,
    "M"
)


# Test 2 - Higher tool wear
test_machine(
    303.0,
    312.0,
    1500,
    60.0,
    200,
    "H"
)


# Test 3 - More extreme operating conditions
test_machine(
    304.0,
    313.0,
    1200,
    70.0,
    250,
    "L"
)