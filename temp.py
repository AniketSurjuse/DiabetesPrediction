# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open(r"C:\Users\LINOVA\Desktop\diabetes\Diabetes_prediction.pckl","rb"))

def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.array(input_data)
    input_data_reshaped =  input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if prediction[0]==1:
        return "The person is diabetic"
    else:
        return "the person is not diabetic"
    
    

def main():
    #giving title
    st.title("Diabetes Prediction Web App")
    
    #getting input data
    
    preg = st.text_input("preg")
    glucose = st.text_input("glucose")
    bp = st.text_input("Blood Pressure")
    skinthickness = st.text_input("SkinThickness")
    insulin = st.text_input("Insulin Level")
    bmi = st.text_input("BMI")
    pedigree = st.text_input("Pegigree")
    age = st.text_input("Age")
    
    #code for prediction
    diagnosis =''
    if st.button("Diabetes Test Result"):
        diagnosis = diabetes_prediction([preg,glucose,bp,skinthickness,insulin,bmi,pedigree,age])
    
    
    st.success(diagnosis)
    
    
    
if __name__ =='__main__':
    main()
    
    
    