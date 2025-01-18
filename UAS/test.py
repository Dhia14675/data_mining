import pandas as pd
from joblib import load

# Load model and encoders
model = load("XGB_model.pkl")
label_encoders = load("label_encoders.pkl")

# Manual input for testing
input_data = pd.DataFrame(
    {
        "Gender": ["Male"],  # Replace with actual input
        "Age": [25],
        "Occupation": ["Engineer"],
        "Sleep Duration": [6.0],
        "Quality of Sleep": [6],
        "Physical Activity Level": [50],
        "Stress Level": [10],
        "BMI Category": ["Normal"],
        "Heart Rate": [75],
        "Daily Steps": [8000],
        "SYSTOLIC": [120.0],
        "DIASTOLIC": [80.0],
    }
)

# Encoding categorical variables
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

expected_columns = [
    "Age", "Sleep Duration", "Quality of Sleep", "Physical Activity Level",
    "Stress Level", "Heart Rate", "Daily Steps", "SYSTOLIC", "DIASTOLIC",
    "Gender", "Occupation", "BMI Category"
]

input_data = input_data[expected_columns]

# Convert to numpy array for prediction
input_array = input_data.values

# Make prediction
prediction = model.predict(input_array)[0]

# Map prediction to class label
disorder_map = {
    1: "No Disorder",
    2: "Sleep Apnea",
    0: "Insomnia"
}
result = disorder_map.get(prediction, "Unknown")

print(f"Prediction: Sleep Disorder - {result}")
