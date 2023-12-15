
# pip install streamlit 
# > streamlit run app.py

import os 
import joblib 
from fastapi import FastAPI
from pathlib import Path 
import streamlit as st 

os.chdir(Path(__file__).parent)



def load_model():
    model = joblib.load("./models/model_linear_reg_v2.jlb")
    return model


def main():

    # 1. Load the model 
    model = load_model() 

    # 2. Write a title
    st.title("Welcome by area prediction application")

    st.write("""
            ### Project Description
             We have already trained the model and now you can predict the area price
            """)
    
    # 3. Add Text Box for area
    area = int(st.text_input("Area", 50))


    # 4. Add a submit Button 
    if st.button("Predict"):

        # Predict the price
        predicted_price = int(model.predict( [ [area]]))

        # Show the predicted price
        st.success(f"The price for the provided area is: {predicted_price}")




if __name__ == "__main__":
    main()