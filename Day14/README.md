#  House Price Prediction (California Housing Dataset)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An end-to-end Machine Learning project predicting median house values in California districts using built-in scikit-learn datasets, regression algorithms, and standard evaluation techniques.



## Table of Contents
- [Overview](#overview)
- [Dataset Summary](#dataset-summary)
- [Project Architecture & Repository Structure](#project-architecture--repository-structure)
- [Key Features & Exploratory Data Analysis](#key-features--exploratory-data-analysis)
- [Model Performance & Evaluation](#model-performance--evaluation)
- [Installation & Usage](#installation--usage)
- [Project Deliverables](#project-deliverables)



##  Overview
This project builds a regression workflow to predict house prices (`MedHouseVal`) based on demographic and structural features across California census block groups.

### Objectives:
1. Perform Exploratory Data Analysis (EDA) and analyze feature correlations.
2. Preprocess numerical features using `StandardScaler`.
3. Train baseline Linear Regression and Random Forest Regressor models.
4. Evaluate predictive performance using $R^2$ Score and Root Mean Squared Error (RMSE).
5. Export trained models using `joblib` for future deployment.



##  Dataset Summary
* **Source:** `sklearn.datasets.fetch_california_housing`
* **Target Variable:** `MedHouseVal` (Median house value for California districts, expressed in $100,000s).
* **Feature Set:**
  * `MedInc`: Median income in block group
  * `HouseAge`: Median house age in block group
  * `AveRooms`: Average number of rooms per household
  * `AveBedrms`: Average number of bedrooms per household
  * `Population`: Block group population
  * `AveOccup`: Average number of household members
  * `Latitude`: Block group latitude
  * `Longitude`: Block group longitude



##  Project Architecture & Repository Structure


house-price-prediction/
│
├── notebooks/
│   └── house_price_prediction.ipynb   # Main Jupyter Notebook
├── models/
│   ├── house_price_model.pkl          # Trained Random Forest Model
│   └── scaler.pkl                     # Saved StandardScaler instance
├── screenshots/
│   ├── correlation_heatmap.png        # Feature correlation plot
│   ├── actual_vs_predicted.png        # Actual vs Predicted house values plot
│   └── feature_importance.png         # Feature importance bar chart
├── README.md                          # Project Documentation
└── requirements.txt                   # Project Dependencies