# AutoWorth AI — ML-Based Car Price Estimator

🔗 [Live Demo](https://autoworthai.streamlit.app/) | [API](https://autoworth-ai-ml-based-car-price-estimator.onrender.com) | [Notebook](https://github.com/HARSHIDS-4/AutoWorthAI)

---

Predicts used car market prices from 13 vehicle attributes using a Random Forest pipeline trained on 426K+ Craigslist listings, served through a deployed FastAPI backend and Streamlit frontend.

---

## Results

| Model | R² | MAE |
|---|---|---|
| Linear Regression (Baseline) | 0.719 | $5,279 |
| XGBoost (best variant) | 0.841 | $3,480 |
| **Random Forest — Final** | **0.875** | **$2,691** |

## Stack
`Python` `FastAPI` `Streamlit` `scikit-learn` `Pydantic` `Joblib` `Render`

## Run Locally
```bash
git clone https://github.com/HARSHIDS-4/AutoWorthAI.git
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
streamlit run frontend.py
```

> Model artifact not included. Download dataset from [Kaggle](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data), run `Car_Price_Predictor.ipynb`, move generated `.joblib` to `model/`.
