import pickle
import numpy as np
import os

# Load the model (this line looks for diabetes_model.pkl in the same folder)
with open("diabetes_model (1).pkl", "rb") as file:
    model = pickle.load(file)

# Prediction function
def predict_diabetes(input_data):
     prediction = model.predict([input_data])[0]
     confidence = max(model.predict_proba([input_data])[0])
     return prediction, confidence

