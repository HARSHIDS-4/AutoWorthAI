# AutoWorth AI

ML-Based Car Price Estimator

AutoWorth AI is a end-to-end machine learning application that estimates the price of a used car from structured vehicle attributes. It combines a FastAPI backend, a Streamlit front end, Pydantic-based request validation, and a scikit-learn preprocessing and regression pipeline for predictions.

## Executive Summary

This project demonstrates the implementation of an applied ML product, not just a standalone model. The system accepts structured vehicle details, validates and normalizes the input, derives car age automatically, and serves predictions through a clean REST API.

## What This Project Shows

- End-to-end machine learning application design
- API development with FastAPI
- Form-driven UI with Streamlit
- Input validation and normalization with Pydantic
- Model serving from a serialized artifact
- Clean separation between frontend, backend, schema, and model logic

## Core Features

- Predicts a used car price from structured vehicle attributes
- Automatically computes car age from the provided model year
- Validates key fields such as year, odometer, manufacturer, state, and cylinders
- Normalizes categorical inputs such as model, type, and paint color
- Exposes a reusable prediction API for integration with other apps
- Provides a lightweight UI for interactive use

## Architecture

The system is organized into four main layers:

1. `frontend.py` - Streamlit application for collecting user input and displaying predictions
2. `app.py` - FastAPI service exposing health, version, and prediction endpoints
3. `schema/` - Pydantic request and response models
4. `model/` - Prediction logic that loads the trained model artifact and returns the final estimate

## Technology Stack

- Python
- FastAPI
- Streamlit
- Pydantic
- pandas
- scikit-learn
- NumPy
- requests
- Uvicorn

## Input Features

The API accepts the following car attributes:

- year
- manufacturer
- model
- condition
- fuel
- odometer
- title_status
- transmission
- drive
- type
- paint_color
- state
- no_of_cylinders

The backend also derives:

- car_age = current year - year

## Validation And Normalization

The request schema applies strict validation to keep predictions reliable:

- `year` must be between 1980 and the current year
- `odometer` must be between 0 and 300000
- `manufacturer` and `state` must match allowed values defined in `config/field_values.py`
- `model`, `type`, and `paint_color` are normalized to `other` when the provided value is not in the supported list
- `condition`, `fuel`, `title_status`, `transmission`, and `drive` are constrained to predefined categories

## API Endpoints

### `GET /`

Returns a simple service message confirming that the API is running.

### `GET /version`

Returns the model version and whether the model artifact is loaded successfully.

### `POST /predict`

Accepts a car payload and returns a predicted price.

Example response:

```json
{
  "predicted_price": 15000.0
}
```

## Project Structure

```text
AutoWorth AI - Intelligent Used Car Price Prediction System/
├── app.py
├── frontend.py
├── requirements.txt
├── config/
│   └── field_values.py
├── model/
│   └── predict.py
├── schema/
│   ├── user_input.py
│   └── prediction_response.py
└── model artifact
    └── car_price_prediction.pkl
```

## Getting Started

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI backend

```bash
uvicorn app:app --reload --port 8000
```

### 4. Run the Streamlit frontend

```bash
streamlit run frontend.py
```

The Streamlit app sends prediction requests to `http://127.0.0.1:8000/predict`, so the FastAPI service should be running first.

## Example API Request

```bash
curl -X POST "http://127.0.0.1:8000/predict" ^
  -H "Content-Type: application/json" ^
  -d "{
    \"year\": 2018,
    \"manufacturer\": \"toyota\",
    \"model\": \"camry\",
    \"condition\": \"good\",
    \"fuel\": \"gas\",
    \"odometer\": 50000,
    \"title_status\": \"clean\",
    \"transmission\": \"automatic\",
    \"drive\": \"fwd\",
    \"type\": \"sedan\",
    \"paint_color\": \"white\",
    \"state\": \"ca\",
    \"no_of_cylinders\": 4
  }"
```

## Model Behavior

The predictor loads the serialized preprocessing and regression pipeline from `car_price_prediction.pkl` and generates a final price estimate after transforming categorical and numerical features.

## Model Performance (Baseline)

| Metric | Value |
|--------|-------|
| R² Score | 0.7190100886808364 |
| MAE | 5279.539151510923 |
| MSE | 56751592.44492194 |

## Deployment

The backend API can be deployed using platforms such as Render or Railway using:

```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

The frontend can be deployed separately using Streamlit Community Cloud.

## Key Engineering Highlights

- Clear backend/frontend separation
- Request validation using Pydantic
- Reusable prediction API
- Automatic feature engineering
- Deployment-ready FastAPI structure

## Notes

- The allowed categorical values are defined in `config/field_values.py`
- The request and response contracts live in `schema/`
- The frontend expects the API to be available locally on port `8000`

## Future Improvements

- Add Docker support for one-command deployment
- Add automated tests for validation and prediction endpoints
- Expose the API through a hosted deployment
- Add feature importance or explanation output for predictions
- Persist model metrics and training metadata alongside the artifact
