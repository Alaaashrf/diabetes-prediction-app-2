import streamlit as st
import numpy as np
import joblib

model = joblib.load('diabetes_model.pkl')

st.title('Diabetes Prediction App 🩺')
st.write("Enter the patient's medical data below:")

glucose = st.number_input('Glucose', min_value=0)
bmi = st.number_input('BMI', min_value=0.0)
age = st.number_input('Age', min_value=0)
insulin = st.number_input('Insulin', min_value=0)
bp = st.number_input('Blood Pressure', min_value=0)

if st.button('Predict'):
    data = np.array([[glucose, bmi, age, insulin, bp]])
    prediction = model.predict(data)
    
    if prediction[0] == 1:
        st.error('⚠️ Prediction: Diabetic')
    else:
        st.success('✅ Prediction: Not Diabetic')