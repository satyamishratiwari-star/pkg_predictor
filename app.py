import streamlit as st
import joblib
import numpy as np
import pandas as pd
import streamlit as st
#going to load model
model=joblib.load("model__lr.joblib")

st.title("Model Deployement using streamlit")

# adding cgpa input box
cgpa=st.number_input("ENTER YOUR CGPA:  ")

# Adding Button for Prediction
if st.button("PREDICT"):
    cgpa=np.array([[cgpa]])
    prediction=model.predict(cgpa)
    st.success(f"YOUR PAKAGE IS : {prediction}")
