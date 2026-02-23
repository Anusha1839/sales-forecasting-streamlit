# sales-forecasting-streamlit
# Sales Forecasting using Prophet (Deployed Streamlit App)

Live Application:
https://anusha1839-sales-forecasting-streamlit-app-d2rj09.streamlit.app/

---

## Project Overview

This project focuses on building an end-to-end time series sales forecasting system using Facebook Prophet. The goal is to predict future sales based on historical transaction data and deploy the trained model as a live web application using Streamlit.

The application dynamically generates future forecasts and provides business insights such as projected revenue and model accuracy.

---

## Problem Statement

Businesses need accurate sales forecasts to support:

- Inventory planning  
- Revenue estimation  
- Demand forecasting  
- Strategic decision making  

This project builds a machine learning-based forecasting model to predict the next 90 days of sales using historical data.

---

## Technologies Used

- Python  
- Prophet (Time Series Forecasting)  
- Pandas  
- Matplotlib  
- Scikit-learn  
- Streamlit  
- Power BI (for business dashboard)  

---

## Project Workflow

- Data preprocessing and cleaning  
- Aggregation of daily sales  
- Exploratory Data Analysis (trend and seasonality detection)  
- Train-test split (80-20)  
- Model training using Prophet  
- Model evaluation using MAE  
- Forecast generation for future periods  
- Deployment as an interactive Streamlit web app  

---

## Model Evaluation

The model was evaluated using Mean Absolute Error (MAE) on validation data.

- Model MAE (Validation Period): 18,292  

This indicates the average deviation between predicted and actual sales during the testing period.

---

## Key Features of the Streamlit App

- Dynamic forecast generation  
- User-selectable forecast period  
- Sales forecast visualization with confidence interval  
- Total forecasted revenue calculation  
- Model accuracy display  
- Clean and interactive web interface  

---

## Business Insights

- The model captures overall sales trend and seasonality patterns  
- Confidence intervals provide uncertainty estimation  
- Forecast helps estimate revenue for the next 90 days  
- Model performance evaluated on unseen validation data  

---

## How to Run Locally

1. Clone the repository  
2. Create a virtual environment  
3. Install dependencies:

pip install -r requirements.txt

4. Run the app:

streamlit run app.py

---

## Future Improvements

- Incorporating holiday effects  
- Adding external regressors (promotions, campaigns)  
- Comparing Prophet with XGBoost or LSTM  
- Enhancing UI with advanced visualizations  

---

## Author

Dhanusha Katakam Ediga 
Aspiring Data Analyst| Data Scientist | AI Engineer

linkedIn : www.linkedin.com/in/dhanusha-k-3756ab341
GitHub: https://github.com/Anusha1839 
