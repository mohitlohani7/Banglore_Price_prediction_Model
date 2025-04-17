import streamlit as st
import pickle
import numpy as np
import json

# Load model
with open('banglore_home_prices_model.pickle', 'rb') as f:
    model = pickle.load(f)

# Load columns data
with open("columns.json", "r") as f:
    columns_data = json.load(f)

# Extract location, area, and availability columns
locations = columns_data['location_columns']
areas = columns_data['area_columns']
availability_options = columns_data['availability_columns']

# Title
st.title("🏡 Bangalore House Price Prediction")
st.markdown("A simple ML-powered app to estimate house prices in Bangalore.")

# Input Section
st.header("📋 Enter Property Details:")

location = st.selectbox("📍 Location", sorted(locations))
area_type = st.selectbox("🏗️ Area Type", sorted(areas))
availability = st.selectbox("📆 Availability", sorted(availability_options))
sqft = st.number_input("📐 Square Footage", min_value=300, max_value=10000, step=10)
bhk = st.selectbox("🛏️ BHK (Bedrooms)", [1, 2, 3, 4, 5])
bath = st.selectbox("🛁 Bathrooms", [1, 2, 3, 4])

# Preprocess input to match training data structure
def preprocess_input(location, area_type, availability, sqft, bhk, bath):
    # Assuming the model expects a one-hot encoded vector
    input_data = np.zeros(len(locations) + len(areas) + len(availability_options) + 3)

    # Set basic features
    input_data[0] = sqft
    input_data[1] = bhk
    input_data[2] = bath

    # Encode location
    if location in locations:
        loc_index = locations.index(location)
        input_data[3 + loc_index] = 1

    # Encode area type
    if area_type in areas:
        area_index = areas.index(area_type)
        input_data[3 + len(locations) + area_index] = 1

    # Encode availability
    if availability in availability_options:
        avail_index = availability_options.index(availability)
        input_data[3 + len(locations) + len(areas) + avail_index] = 1

    return input_data.reshape(1, -1)

# Predict Button
if st.button("🚀 Estimate Price"):
    input_features = preprocess_input(location, area_type, availability, sqft, bhk, bath)
    price = model.predict(input_features)[0]
    st.success(f"🏷️ Estimated Price: ₹ {round(price, 2)} Lakhs")
