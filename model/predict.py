import pickle
from pathlib import Path
import pandas as pd

_CURRENT_DIR = Path(__file__).resolve().parent
_PROJECT_DIR = _CURRENT_DIR.parent
_WORKSPACE_DIR = _PROJECT_DIR.parent

_MODEL_CANDIDATES = [
    _CURRENT_DIR / "car_price_prediction_rf.pkl",
    _PROJECT_DIR / "car_price_prediction_rf.pkl",
    _WORKSPACE_DIR / "car_price_prediction_rf.pkl",
]

_MODEL_PATH = next((path for path in _MODEL_CANDIDATES if path.exists()), None)
if _MODEL_PATH is None:
    searched = ", ".join(str(p) for p in _MODEL_CANDIDATES)
    raise FileNotFoundError(
        f"Model file 'car_price_prediction_rf.pkl' not found. Searched: {searched}"
    )

with _MODEL_PATH.open("rb") as f:
    car_price = pickle.load(f)

MODEL_VERSION='1.0.0'

def predict_output(car:dict):
    input_values=pd.DataFrame([car])
    prediction=car_price.predict(input_values)[0]
    prediction=max(0,prediction)
    return {"predicted_price": round(prediction,2)}