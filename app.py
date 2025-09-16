<<<<<<< HEAD
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("KNN_Heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

# App title
st.title("Heart Stroke Prediction By Vaibhav ❤️")
st.markdown("Provide the following details..")

# Input fields
age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("SEX", ['Male', 'Female'])
Chest_Pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
Resting_BP = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)

Cholestrol = st.number_input("Cholestrol (mg/DL)", 100, 600, 200)
Fasting_BS = st.selectbox("Fasting Blood Sugar > 120 mg/DL", [0, 1])
Resting_ECG = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
Max_HR = st.slider("Max Heart Rate", 60, 220, 150)
Exercise_angina = st.selectbox("Exercise-Induced Angina", ["YES", "NO"])
OldPeak = st.slider("OldPeak (ST Depression)", 0.0, 6.0, 1.0)
St_slope = st.selectbox("ST Slope", ["UP", "FLAT", "DOWN"])

# Prediction block
if st.button("Predict 🔍"):
    raw_input = {
        'Age': age,
        'RestingBP': Resting_BP,
        'Cholesterol': Cholestrol,
        'FastingBS': Fasting_BS,
        'MaxHR': Max_HR,
        'Oldpeak': OldPeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + Chest_Pain: 1,
        'RestingECG_' + Resting_ECG: 1,
        'ExerciseAngina_' + Exercise_angina: 1,
        'ST_Slope_' + St_slope: 1
    }

    # Convert input into DataFrame
    input_df = pd.DataFrame([raw_input])

    # Add missing columns as 0
    for col in expected_columns:
        if col not in input_df:
            input_df[col] = 0

    # Arrange columns in correct order
    input_df = input_df[expected_columns]

    st.write("Final Input DataFrame:", input_df)

    # Scale and predict
    scaled_input = scaler.transform(input_df)   
    Prediction = model.predict(scaled_input)[0]

    # Display result
    if Prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("😮‍💨 You are Safe")
=======
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("KNN_Heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

# App title
st.title("Heart Stroke Prediction By Vaibhav ❤️")
st.markdown("Provide the following details..")

# Input fields
age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("SEX", ['Male', 'Female'])
Chest_Pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
Resting_BP = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)

Cholestrol = st.number_input("Cholestrol (mg/DL)", 100, 600, 200)
Fasting_BS = st.selectbox("Fasting Blood Sugar > 120 mg/DL", [0, 1])
Resting_ECG = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
Max_HR = st.slider("Max Heart Rate", 60, 220, 150)
Exercise_angina = st.selectbox("Exercise-Induced Angina", ["YES", "NO"])
OldPeak = st.slider("OldPeak (ST Depression)", 0.0, 6.0, 1.0)
St_slope = st.selectbox("ST Slope", ["UP", "FLAT", "DOWN"])

# Prediction block
if st.button("Predict 🔍"):
    raw_input = {
        'Age': age,
        'RestingBP': Resting_BP,
        'Cholesterol': Cholestrol,
        'FastingBS': Fasting_BS,
        'MaxHR': Max_HR,
        'Oldpeak': OldPeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + Chest_Pain: 1,
        'RestingECG_' + Resting_ECG: 1,
        'ExerciseAngina_' + Exercise_angina: 1,
        'ST_Slope_' + St_slope: 1
    }

    # Convert input into DataFrame
    input_df = pd.DataFrame([raw_input])

    # Add missing columns as 0
    for col in expected_columns:
        if col not in input_df:
            input_df[col] = 0

    # Arrange columns in correct order
    input_df = input_df[expected_columns]

    st.write("Final Input DataFrame:", input_df)

    # Scale and predict
    scaled_input = scaler.transform(input_df)
    Prediction = model.predict(scaled_input)[0]

    # Display result
    if Prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("😮‍💨 You are Safe")
>>>>>>> e99236e3e6abee609837811c5f0cd6e82be48ab1
