# AI Predictive Maintenance System

An AI-based predictive maintenance system for industrial equipment that analyzes sensor and operational data to predict potential machine failures, estimate failure probability, classify equipment risk, and provide maintenance recommendations through an interactive Streamlit dashboard.

---

## 📌 Project Overview

Unexpected industrial equipment failures can cause production downtime, maintenance costs, and operational losses.

This project develops an AI-based predictive maintenance system that uses machine learning to analyze equipment operating conditions and identify machines that may be at risk of failure.

The system provides:

- Machine failure prediction
- Failure probability estimation
- Equipment risk classification
- Maintenance recommendations
- Interactive equipment health monitoring
- Streamlit-based dashboard

---

## 🎯 Objectives

The main objectives of this project are:

- Develop a machine learning model for industrial equipment failure prediction.
- Analyze equipment sensor and operational data.
- Preprocess and prepare industrial equipment data for machine learning.
- Compare multiple machine learning models.
- Predict potential equipment failures before they occur.
- Generate failure probability and equipment risk levels.
- Provide actionable maintenance recommendations.
- Develop an interactive dashboard for equipment health monitoring.

---

## ✨ Features

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Statistical analysis
- Correlation analysis
- Machine learning-based failure prediction
- Logistic Regression baseline model
- Random Forest classification model
- Model performance comparison
- Confusion matrix evaluation
- Feature importance analysis
- Failure probability estimation
- Equipment risk classification
- Maintenance recommendations
- Interactive Streamlit dashboard
- Git and GitHub version control

---

## 📊 Dataset

This project uses the **AI4I 2020 Predictive Maintenance Dataset**.

The dataset contains **10,000 industrial equipment records** with sensor and operational measurements.

### Important Features

| Feature | Description |
|---|---|
| Air temperature [K] | Ambient air temperature |
| Process temperature [K] | Equipment process temperature |
| Rotational speed [rpm] | Machine rotational speed |
| Torque [Nm] | Applied machine torque |
| Tool wear [min] | Tool usage/wear time |
| Type | Machine/product type |
| Machine failure | Target variable |

### Target Variable

```text
Machine failure

0 → No Failure
1 → Failure