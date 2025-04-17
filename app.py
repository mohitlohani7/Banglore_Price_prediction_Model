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
except FileNotFoundError:
    st.error("❌ Columns file not found. Please ensure 'columns.json' is in the same directory.")
    st.stop()
