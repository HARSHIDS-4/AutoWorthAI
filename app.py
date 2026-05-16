from fastapi import FastAPI
from schema.user_input import Car
from fastapi.responses import JSONResponse
from model.predict import predict_output, MODEL_VERSION, car_price
from schema.prediction_response import PredictionResponse

app=FastAPI()


@app.get("/")
def home():
    return {"message": "Car Price Prediction API"}

@app.get("/version")
def version():
    return {
        "status": "OK",
        "model_version": MODEL_VERSION,
        "model loaded": car_price is not None
        }

@app.post("/predict",response_model=PredictionResponse)
def predict_price(car:Car):
    user_input={
        "year": car.year,
        "manufacturer": car.manufacturer,
        "model": car.model,
        "condition": car.condition,
        "fuel": car.fuel,
        "title_status": car.title_status,
        "transmission": car.transmission,
        "drive": car.drive,
        "type": car.type,
        "odometer": car.odometer,
        "paint_color": car.paint_color,
        "state": car.state,
        "car_age": car.car_age,
        "no_of_cylinders": car.no_of_cylinders
    }
    try: 
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200,content=prediction)

    except Exception as e:
        return JSONResponse(status_code=500,content={"error": str(e)})

        