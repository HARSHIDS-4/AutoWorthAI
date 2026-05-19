import pickle
from pathlib import Path
import pandas as pd
import joblib

_CURRENT_DIR = Path(__file__).resolve().parent
_PROJECT_DIR = _CURRENT_DIR.parent
_WORKSPACE_DIR = _PROJECT_DIR.parent

# Look for common model filenames (pkl and joblib) in project and user's Downloads
_CANDIDATE_NAMES = [
    "car_price_prediction_rf.pkl",
    "car_price_prediction.pkl",
    "car_price_prediction_rf.joblib",
    "car_price_prediction_rf_xgb.joblib",
    "car_price_prediction_rf_xgb.pkl",
]

_MODEL_CANDIDATES = []
for name in _CANDIDATE_NAMES:
    _MODEL_CANDIDATES.extend([
        _CURRENT_DIR / name,
        _PROJECT_DIR / name,
        _WORKSPACE_DIR / name,
        Path.home() / "Downloads" / name,
    ])

_MODEL_PATH = next((path for path in _MODEL_CANDIDATES if path.exists()), None)
if _MODEL_PATH is None:
    searched = ", ".join(str(p) for p in _MODEL_CANDIDATES)
    raise FileNotFoundError(
        f"Model file not found. Searched: {searched}"
    )

# Load with joblib for .joblib files, otherwise use pickle
if _MODEL_PATH.suffix in (".joblib", ".gz"):
    car_price = joblib.load(_MODEL_PATH)
else:
    with _MODEL_PATH.open("rb") as f:
        car_price = pickle.load(f)

MODEL_VERSION = "1.0.0"

def predict_output(car:dict):
    input_values=pd.DataFrame([car])
    prediction=car_price.predict(input_values)[0]
    prediction=max(0,prediction)
    return {"predicted_price": round(prediction,2)}