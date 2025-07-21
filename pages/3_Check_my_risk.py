import streamlit as st
import pandas as pd
from datetime import datetime
import os
import sys

# Add parent directory to system path so Python can find model.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model import predict_diabetes

st.title("🩺 Diabetes Risk Checker")
st.subheader("Fill in the details below to check your risk")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose Level (mg/dL)", min_value=50, max_value=300, value=100)
blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=40, max_value=200, value=80)
skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0.0, step=1.0)
insulin = st.number_input("Insulin Level", min_value=0.0, max_value=900.0, value=80.0, step=1.0)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=22.5, step=0.1)
diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, step=0.01)
age = st.number_input("Age", min_value=1, max_value=120, value=30)


if st.button("✅ Check My Risk"):
    if glucose == 0 or bmi == 0:
        st.error("Glucose and BMI must be greater than 0.")
    else:
        # Save input
        input_data = {
            "Pregnancies": pregnancies,
            "Glucose": glucose,
            "Blood_pressure": blood_pressure,
            "SkinThickness": skin_thickness,
            "Insulin": insulin,
            "BMI": bmi,
            "DiabetesPedigreeFunction": diabetes_pedigree_function,
            "Age": age,

        }

        # Save to CSV
        new_row = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            **input_data,
        }

        file_path = "risk_data.csv"
        df_new = pd.DataFrame([new_row])
        if os.path.exists(file_path):
            df_existing = pd.read_csv(file_path)
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        else:
            df_combined = df_new
        df_combined.to_csv(file_path, index=False)

        st.success("✔️ Your data has been recorded!")

        # Predict
        risk_level, confidence = predict_diabetes(list(input_data.values()))

        st.subheader("🧠 Prediction Results")
        st.success(f"**Risk Level:** {risk_level}")
        st.info(f"**Prediction Confidence:** {round(confidence * 100, 2)}%")

        st.subheader("📋 Lifestyle Recommendations")
        if risk_level == "Low":
            st.markdown("✅ Keep up your healthy lifestyle.")
        elif risk_level == "Medium":
            st.markdown("⚠️ Moderate risk. Improve diet and increase exercise.")
        elif risk_level == "High":
            st.error("❗ High risk. Please consult a doctor.")
        else:
            st.warning("No recommendation available.")

        with st.expander("🔎 Review Your Submitted Info"):
            for key, val in input_data.items():
                st.write(f"**{key}**: {val}")
