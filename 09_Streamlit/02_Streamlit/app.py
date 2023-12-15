
# pip install streamlit 
# > streamlit run app.py

import os 
import pandas as pd 
from fastapi import FastAPI
from pathlib import Path 
import streamlit as st 

os.chdir(Path(__file__).parent)



def get_dataframe():
    df = pd.read_csv("./multi_variate.csv")
    return df 




# Get the whole Dataframe
df = get_dataframe() 


# Sidebar
# ~~~~~~~
st.sidebar.header("Filter the data")

area = st.sidebar.multiselect(
    "Select the area",
    options=df["area"].unique(),
    default=df["area"].unique()
)

roomcount = st.sidebar.multiselect(
    "Select the Room Count",
    options=df["roomcount"].unique(),
    default=df["roomcount"].unique()
)

# select the required data from my filters
df_selected = df.query("area == @area & roomcount == @roomcount")


# Web Page
# ~~~~~~~~
st.title(" Area Price Prediction Dashboard")
st.markdown("---")


st.markdown("## Information")


# Calculate the aggregations
total_area = int(df_selected["area"].sum())
avg_price = round(float(df_selected["price"].mean()), 2)
message = "This is important"



# Split the ara into 3x columns
left_col, middle_col, right_col =  st.columns(3)

with left_col:
    st.subheader("Total area")
    st.subheader(total_area)

with middle_col:
    st.subheader("AVG Price")
    st.subheader(avg_price)

with right_col:
    st.subheader("Message")
    st.subheader(message)


st.markdown("## Data Frame")
st.dataframe(df_selected)
