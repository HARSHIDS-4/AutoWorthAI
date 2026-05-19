# AutoWorth AI
### ML-Based Used Car Price Estimator

An end-to-end ML application that predicts used car prices from structured vehicle attributes via a REST API and interactive web interface.

🔗 **[Live Demo](https://autoworthai.streamlit.app/)** | **[API](https://autoworth-ai-ml-based-car-price-estimator.onrender.com)**

---

## Tech Stack
Python, FastAPI, Streamlit, scikit-learn, Pydantic, Joblib, Uvicorn, Render

---

## Model Performance

| Model | R² | MAE |
|---|---|---|
| Linear Regression (Baseline) | 0.719 | $5,279 |
| XGBoost (default) | 0.841 | $3,480 |
| XGBoost (tuned) | 0.829 | $3,629 |
| XGBoost + Log Transform | 0.813 | $3,595 |
| **Random Forest (150 trees)** | **0.875** | **$2,691** |

Random Forest deployed as final model. XGBoost underperformed due to high-dimensional sparse OHE features.

---

## Architecture

Frontend (Streamlit) → Backend API (FastAPI) → sklearn Pipeline → Joblib Model

---

## Run Locally

```bash
git clone https://github.com/HARSHIDS-4/AutoWorthAI.git
cd AutoWorthAI
pip install -r requirements.txt
uvicorn app:app --reload --port 8000   # backend
streamlit run frontend.py              # frontend
```

> **Note:** `.joblib` file not included due to size. Fork the repo, download `vehicles.csv` from [Kaggle](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data), run `Car_Price_Predictor.ipynb`, and move the generated `car_price_prediction.joblib` into `model/`.

---

## Dataset
[Craigslist Cars & Trucks — Austin Reese](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data) — 426K listings, 26 features

---

## Author
Harshi Gupta | [LinkedIn](https://linkedin.com/in/harshi-gupta-2726a1349) | [GitHub](https://github.com/HARSHIDS-4)
