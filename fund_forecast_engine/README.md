# Preqin Private Markets Data Science Projects

This repository showcases three full-stack data science prototypes tailored to private markets analytics. These projects simulate the kind of ML pipelines and analytical tools developed at Preqin, a part of BlackRock.

Each project follows best practices for data modeling, transformation, and interpretability — and can be extended to real-world private equity, infrastructure, and hedge fund datasets.

---

## 🔹 1. Private Equity Fund Forecast Engine

**Goal:** Predict capital calls and distributions for private equity funds to support LP cash planning.

**Highlights:**
- IRR-based curve modeling
- Time-series forecasting using SARIMA
- Simulated output for quarterly LP cash flow scenarios

📂 Folder: `/fund_forecast_engine/`

---

## 🔹 2. Private Market Valuation Normalizer

**Goal:** Standardize NAV values and flag valuation outliers across vintage-year private market funds.

**Highlights:**
- Residual-based anomaly detection
- Regression filtering with volatility bands
- Validation rules + synthetic NAV dataset

📂 Folder: `/valuation_normalizer/`

---

## 🔹 3. Investor Profile Clustering & Allocation Recommender

**Goal:** Cluster LPs based on risk and liquidity profiles, and recommend private market allocations.

**Highlights:**
- Gaussian Mixture Modeling (GMM)
- Custom allocation logic across PE, infra, RE
- Interactive API-ready prototype

📂 Folder: `/investor_clustering_recommender/`

---

## 📦 How to Run

Each project is self-contained and runs via Jupyter Notebook.

```bash
cd project_folder
pip install -r requirements.txt
jupyter notebook
```
