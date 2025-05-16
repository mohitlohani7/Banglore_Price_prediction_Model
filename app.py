import streamlit as st
import pickle
import numpy as np
import json
import os

# Load model
try:
    with open('banglore_home_prices_model.pickle', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("❌ Model file not found. Please ensure 'banglore_home_prices_model.pickle' is in the same directory.")
    st.stop()

# Load columns
try:
    with open("columns.json", "r") as f:
        columns_data = json.load(f)
        data_columns = columns_data['data_columns']
        location_list = data_columns[3:]  # Assuming first 3 are sqft, bath, bhk
except FileNotFoundError:
    st.error("❌ Columns file not found. Please ensure 'columns.json' is in the same directory.")
    st.stop()

# Streamlit UI
st.title("🏠 Bangalore House Price Predictor")

# Inputs
location = st.selectbox("Select Location", sorted(location_list))
sqft = st.number_input("Total Square Feet", min_value=300.0, max_value=10000.0, step=10.0)
bath = st.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1)
bhk = st.number_input("Number of BHK", min_value=1, max_value=10, step=1)

if st.button("Predict Price"):
    try:
        # Build feature array
        x = np.zeros(len(data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if location.lower() in [l.lower() for l in location_list]:
            idx = data_columns.index(location.lower())
            x[idx] = 1

        prediction = model.predict([x])[0]
        st.success(f"💰 Estimated Price: ₹ {prediction:,.2f} Lakhs")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
