import streamlit as st
import requests
from datetime import datetime
API_URL="https://autoworthai.onrender.com/predict"

st.title("Car Price Prediction")
st.markdown("Enter the details to predict the car price: ")

#input fields
year=st.number_input("Year",min_value=1980,max_value=datetime.now().year,value=2020)

manufacturer=st.text_input("Manufacturer")

model=st.text_input("Model")

condition=st.selectbox("Condition",['salvage','fair','other','good','excellent','like new','new'])

fuel=st.selectbox("Fuel Type",["gas","diesel","electric","hybrid","other"])

odometer=st.number_input("Odometer Reading",min_value=0,max_value=300000,value=50000)

title_status=st.selectbox("Title Status",["clean","rebuilt","lien","salvage","missing","parts only"])

transmission=st.selectbox("Transmission",["automatic","manual","other"])

drive=st.selectbox("Drive Type",["4wd","fwd","rwd","other"])

type=st.text_input("Type")

paint_color=st.text_input("Paint Color")

state=st.text_input("State")       

no_of_cylinders=st.number_input("Number of Cylinders",min_value=0,max_value=16,value=6)

if st.button("Predict Price"):
    input_data={
        "year": year,
        "manufacturer": manufacturer,
        "model": model,
        "condition": condition,
        "fuel": fuel,
        "title_status": title_status,
        "transmission": transmission,
        "drive": drive,
        "type": type,
        "odometer": odometer,
        "paint_color": paint_color,
        "state": state,
        "no_of_cylinders": no_of_cylinders
    }     

    try:
        response=requests.post(API_URL,json=input_data)
        if response.status_code==200:
            result=response.json()
            st.success(f"Predicted car price: **{result['predicted_price']}**")
           
        else:
           st.error(f"API Error: {response.status_code} - {response.text}")
    
    except requests.exceptions.ConnectionError:
        st.error(f"Error connecting to API: make sure it is running on port 8000")
        