import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('banglore_home_prices_model.pickle', 'rb') as f:
    model = pickle.load(f)

# Title
st.title("🏠 Bangalore House Price Predictor")
st.subheader("Enter the details of the property below:")

# Input Fields
area = st.number_input("Total Area (in sqft)", min_value=300, max_value=10000, step=10)
bhk = st.selectbox("BHK (Bedrooms)", [1, 2, 3, 4, 5])
bath = st.selectbox("Bathrooms", [1, 2, 3, 4])

# Location input dropdown
location = st.selectbox("Location", ['Whitefield', 'Electronic City', 'Indiranagar', 'Koramangala', 'Other'])

# Encode location (Assuming model expects encoded value, adjust if required)
# Example of location encoding (you need to adjust as per model's requirements)
location_dict = {'Whitefield': 0, 'Electronic City': 1, 'Indiranagar': 2, 'Koramangala': 3, 'Other': 4}
location_encoded = location_dict.get(location, 4)

# Prepare input data
input_data = np.array([[area, bhk, bath, location_encoded]])

# Predict price button
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"🏡 Estimated Price: ₹ {round(prediction, 2)} Lakhs")
