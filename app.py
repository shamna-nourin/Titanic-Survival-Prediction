import streamlit as st
from PIL import Image   #to load image
import joblib
import numpy as np


model=joblib.load('titanic_model.pkl')
le1=joblib.load('le1.pkl')
le2=joblib.load('le2.pkl')
scaler=joblib.load('scaler.pkl')

st.title('Titanic Survival Prediction 🚢')
# st.header('Data Analysis')
# st.subheader('Data Description')
st.write("""
Predict whether a passenger would have survived the Titanic disaster
based on passenger details using Machine Learning.
Enter the passenger information below to get a survival prediction.
""")

# st.image(Image.open(r"C:\Users\User\Desktop\DS\Machine Learning\Deployment\istockphoto-503132519-612x612.jpg"))

#user input
pclass=st.number_input('Enter your PClass:')
# sex=st.text_input('Enter your Sex:')
# Dropdown for gender selection
options = ["male", "female"]
sex = st.selectbox("Choose your gender:", options)

age=st.number_input('Enter your Age:')
sibsp=st.number_input('Enter your SibSp:')
Parch=st.number_input('Enter your Parch:')

# Dropdown for Embarked selection (assuming similar logic for Embarked)
embarked_options = ["C", "Q", "S"]  # Modify these options based on your data
Embarked = st.selectbox("Choose your embarkation port:", embarked_options)




if st.button("Predict"):
    if sex and Embarked:  # Check if inputs are not empty
        try:
            sex = le1.transform([sex])[0]
            Embarked = le2.transform([Embarked])[0]
            
            # Model prediction
            prediction = model.predict(scaler.transform([[pclass, sex, age, sibsp, Parch, Embarked]]))[0]
            
            # Check the prediction output format
            if prediction == 1:  # Direct check if prediction is not nested
                st.write("Prediction: Alive")
            else:
                st.write("Prediction: Dead")
        except Exception as e:
            st.error(f"Error in prediction: {e}")



