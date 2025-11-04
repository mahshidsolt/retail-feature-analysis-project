# Retail Sales Analysis with XGBoost

This project analyzes retail sales data to predict **Revenue** and identify which features (like **Price**, **Country**, **Time of Day**, etc.) have the greatest impact on sales performance.  

It uses **XGBoost Regression** for predictive modeling and **feature importance ranking** to understand key sales drivers.

---

## Project Overview

- **Dataset:** Retail transaction data including:
  - Invoice, Stock Code, Description
  - Quantity, Price, Country
  - Derived features like `DayOfWeek`, `Month`, `IsWeekend`, `Hour`, and `TimeOfDay`

---

## Features

- Data cleaning and preprocessing  
- Feature engineering (extracting time-based info)  
- XGBoost Regressor for predicting sales revenue  
- Feature importance ranking  
- Visualizations of model insights  

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
2. online retail dataset on kaggle is used for this analysis.
export from https://www.kaggle.com/datasets/lakshmi25npathi/online-retail-dataset
and convert to csv through data_processing.py
## Dependencies:
pandas, numpy, matplotlib, seaborn, sklearn, xgboost

## Future improvements:
1. build a recommendation system based on xgb regressor
2. Add interactive dashboard (e.g., Plotly / Streamlit)
3. Understand which factors most influence sales and generate insights such as:
  - People buy more during certain hours of the day.
