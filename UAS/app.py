import streamlit as st
import pandas as pd
from joblib import load
import os



model = load("XGB_model.pkl")
label_encoders = load("label_encoders.pkl")
# Title
st.title("Sleep Disorder Prediction")

# Load the model and encoders


# User input
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=100, value=25)
occupation = st.selectbox(
    "Occupation",
    ["Nurse", "Doctor", "Engineer", "Lawyer", "Teacher", "Accountant", 
     "SalesPerson", "Software Engineer", "Scientist", "Sales Representative", "Manager"]
)
sleep_duration = st.number_input("Sleep Duration (hours)", min_value=0.0, max_value=24.0, value=6.0)
quality_of_sleep = st.slider("Quality of Sleep (1-10)", min_value=1, max_value=10, value=6)
physical_activity = st.number_input("Physical Activity Level", min_value=0, max_value=100, value=50)
stress_level = st.slider("Stress Level (1-10)", min_value=1, max_value=10, value=5)
bmi_category = st.selectbox("BMI Category", ["Normal", "Overweight", "Underweight", "Obese"])
heart_rate = st.number_input("Heart Rate", min_value=30, max_value=200, value=75)
daily_steps = st.number_input("Daily Steps", min_value=0, max_value=50000, value=8000)
systolic = st.number_input("SYSTOLIC", min_value=50.0, max_value=200.0, value=120.0)
diastolic = st.number_input("DIASTOLIC", min_value=30.0, max_value=150.0, value=80.0)

# Convert inputs to DataFrame
input_data = pd.DataFrame(
    {
        "Gender": [gender],
        "Age": [age],
        "Occupation": [occupation],
        "Sleep Duration": [sleep_duration],
        "Quality of Sleep": [quality_of_sleep],
        "Physical Activity Level": [physical_activity],
        "Stress Level": [stress_level],
        "BMI Category": [bmi_category],
        "Heart Rate": [heart_rate],
        "Daily Steps": [daily_steps],
        "SYSTOLIC": [systolic],
        "DIASTOLIC": [diastolic],
    }
)

# Encoding categorical variables
try:
    input_data['Gender'] = input_data['Gender'].map({"Female": 0, "Male": 1})
    occupation_mapping = {
        "Nurse": 5, "Doctor": 1, "Engineer": 2, "Lawyer": 3, "Teacher": 10,
        "Accountant": 0, "SalesPerson": 7, "Software Engineer": 9,
        "Scientist": 8, "Sales Representative": 6, "Manager": 4
    }
    input_data['Occupation'] = input_data['Occupation'].map(occupation_mapping)
    bmi_mapping = {
        "Normal": 0, "Overweight": 1, "Underweight": 3, "Obese": 2
    }
    input_data['BMI Category'] = input_data['BMI Category'].map(bmi_mapping)
except Exception as e:
    st.error(f"Error in data encoding: {e}")
    st.stop()

# Ensure input_data columns are in the correct order
expected_columns = [
    "Age", "Sleep Duration", "Quality of Sleep", "Physical Activity Level",
    "Stress Level", "Heart Rate", "Daily Steps", "SYSTOLIC", "DIASTOLIC",
    "Gender", "Occupation", "BMI Category"
]

input_data = input_data[expected_columns]

# Prediction
if st.button("Predict"):
    try:
        input_array = input_data.values
        prediction = model.predict(input_array)[0]

        # Map numerical predictions to class labels
        disorder_map = {
            1: "No Disorder",
            2: "Sleep Apnea",
            0: "Insomnia"
        }

        result = disorder_map.get(prediction, "Unknown")
        st.success(f"Prediction: Sleep Disorder - {result}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
