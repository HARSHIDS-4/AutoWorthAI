# AutoWorth AI

### ML-Based Car Price Estimator

AutoWorth AI is an end-to-end machine learning application that estimates the price of a used car from structured vehicle attributes. The project combines a FastAPI backend, a Streamlit frontend, Pydantic-based request validation, and a scikit-learn preprocessing and regression pipeline for real-time predictions.

---

# Live Deployment

### Frontend (Streamlit)
https://autoworthai.streamlit.app/

### Backend API (Render)
https://autoworth-ai-ml-based-car-price-estimator.onrender.com

---

# Executive Summary

This project demonstrates the implementation of a production-style machine learning application rather than just a standalone notebook model. The system accepts structured vehicle details, validates and normalizes user input, derives engineered features such as car age, and serves predictions through a REST API.

The application showcases practical skills across:

- Machine Learning
- Data Preprocessing
- Backend API Development
- Frontend Integration
- Deployment Engineering
- Input Validation
- Model Serialization

---

# What This Project Demonstrates

- End-to-end machine learning workflow
- REST API development using FastAPI
- Frontend integration using Streamlit
- Data preprocessing and feature engineering
- Request validation using Pydantic
- Model deployment and serving
- Production-oriented project structure

---

# Dataset

Dataset used for training:

- Craigslist Cars & Trucks Dataset  
  https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data

---

# Core Features

- Predicts used car prices from structured vehicle attributes
- Automatically derives `car_age` from manufacturing year
- Handles categorical and numerical preprocessing through a serialized pipeline
- Validates user inputs before prediction
- Normalizes unsupported categories to fallback values where applicable
- Provides reusable prediction API endpoints
- Includes an interactive web interface for real-time usage

---

# System Architecture

The application is organized into multiple layers for separation of concerns:

## 1. Frontend Layer

### `frontend.py`
- Built using Streamlit
- Collects user input
- Sends requests to backend API
- Displays prediction results interactively

---

## 2. Backend API Layer

### `app.py`
- Built using FastAPI
- Exposes REST endpoints
- Handles request validation
- Returns prediction responses

---

## 3. Schema Layer

### `schema/`
Contains Pydantic request and response models:

- `user_input.py`
- `prediction_response.py`

---

## 4. Model Layer

### `model/`
Contains prediction logic and serialized ML artifacts:

- `predict.py`
- `car_price_prediction.pkl`

---

# Technology Stack

## Backend & ML

- Python
- FastAPI
- scikit-learn
- pandas
- NumPy
- Pydantic
- Joblib
- Uvicorn

## Frontend

- Streamlit
- requests

---

# Input Features

The model accepts the following features:

| Feature | Type |
|---|---|
| year | Numerical |
| manufacturer | Categorical |
| model | Categorical |
| condition | Categorical |
| fuel | Categorical |
| odometer | Numerical |
| title_status | Categorical |
| transmission | Categorical |
| drive | Categorical |
| type | Categorical |
| paint_color | Categorical |
| state | Categorical |
| no_of_cylinders | Numerical |

---

# Feature Engineering

The backend automatically derives:

```python
car_age = current_year - year
```

---

# Validation & Normalization

The request schema performs strict validation to improve prediction reliability.

## Validation Rules

- `year` must be between 1980 and current year
- `odometer` must be between 0 and 300000
- `no_of_cylinders` must be within valid limits
- `manufacturer` and `state` must belong to supported values

## Normalization Rules

Unsupported values for:
- `model`
- `type`
- `paint_color`

are normalized to:

```python
"other"
```

---

# Machine Learning Pipeline

The serialized scikit-learn pipeline includes:

- Missing value handling
- One-hot encoding
- Ordinal encoding
- Feature selection
- Linear Regression model

Pipeline components used:

- `SimpleImputer`
- `OneHotEncoder`
- `OrdinalEncoder`
- `SelectKBest`
- `LinearRegression`

---

# Model Performance (Baseline)

| Metric | Value |
|---|---|
| R² Score | 0.7190 |
| MAE | 5279.53 |
| MSE | 56751592.44 |

---

# API Endpoints

## `GET /`

Checks whether the API is running.

### Example Response

```json
{
  "message": "Car Price Prediction API"
}
```

---

## `GET /version`

Returns model version and load status.

---

## `POST /predict`

Accepts vehicle details and returns predicted price.

### Example Request

```json
{
  "year": 2018,
  "manufacturer": "toyota",
  "model": "camry",
  "condition": "good",
  "fuel": "gas",
  "odometer": 50000,
  "title_status": "clean",
  "transmission": "automatic",
  "drive": "fwd",
  "type": "sedan",
  "paint_color": "white",
  "state": "ca",
  "no_of_cylinders": 4
}
```

### Example Response

```json
{
  "predicted_price": 15000.0
}
```

---

# Project Structure

```text
AutoWorthAI/
│
├── app.py
├── frontend.py
├── requirements.txt
│
├── config/
│   └── field_values.py
│
├── model/
│   ├── predict.py
│   └── car_price_prediction.pkl
│
├── schema/
│   ├── user_input.py
│   └── prediction_response.py
│
└── README.md
```

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone <https://github.com/HARSHIDS-4/AutoWorthAI.git>
cd AutoWorthAI
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running The Application

## Start FastAPI Backend

```bash
uvicorn app:app --reload --port 8000
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

## Start Streamlit Frontend

```bash
streamlit run frontend.py
```

---

# Example cURL Request

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

---

# Deployment

## Backend Deployment

The FastAPI backend is deployed on Render using:

```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

---

## Frontend Deployment

The Streamlit frontend is deployed using Streamlit Community Cloud.

---


# Future Improvements

- Add Docker containerization
- Add automated API tests
- Integrate advanced regression models (XGBoost, Random Forest)
- Add model explainability (SHAP)
- Add CI/CD pipeline
- Add database logging for prediction requests
- Add monitoring and analytics

---

# Author

HARSHI GUPTA

---

# License

This project is licensed under the MIT License.
