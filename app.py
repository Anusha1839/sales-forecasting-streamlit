import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from prophet import Prophet

st.title("Sales Forecasting Dashboard")
st.markdown("Dynamic Forecast using Prophet Model")

# Load trained model
with open("prophet_model.pkl", "rb") as f:
    model = pickle.load(f)

# User input for forecast period
period = st.slider("Select Forecast Period (Days)", 30, 180, 90)

# Create future dataframe
future = model.make_future_dataframe(periods=period)
forecast = model.predict(future)

# Show total forecast revenue
future_forecast = forecast.tail(period)
total_sales = future_forecast["yhat"].sum()

st.metric("Total Forecasted Revenue", f"${total_sales:,.0f}")

# Plot forecast
st.subheader("Sales Forecast with Confidence Interval")

plt.figure(figsize=(10,5))
plt.plot(forecast["ds"], forecast["yhat"], label="Predicted Sales")
plt.fill_between(forecast["ds"],
                 forecast["yhat_lower"],
                 forecast["yhat_upper"],
                 alpha=0.3)

plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()

st.pyplot(plt)