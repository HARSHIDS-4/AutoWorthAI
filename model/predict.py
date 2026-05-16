import pickle
import pandas as pd

with open("car_price_prediction.pkl",'rb') as f:
    car_price=pickle.load(f)

MODEL_VERSION='1.0.0'

def predict_output(car:dict):
    input_values=pd.DataFrame([car])
    prediction=car_price.predict(input_values)[0]
    prediction=max(0,prediction)
    return {"predicted_price": round(prediction,2)}