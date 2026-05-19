import pandas as pd
import joblib

car_price = joblib.load(r"C:\Users\hp\OneDrive\Desktop\AutoWorthAI\AutoWorthAI\car_price_prediction_rf_xgb.joblib")

MODEL_VERSION = "1.0.0"

def predict_output(car:dict):
    input_values=pd.DataFrame([car])
    prediction=car_price.predict(input_values)[0]
    prediction=max(0,prediction)
    return {"predicted_price": round(prediction,2)}
