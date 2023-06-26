import pandas as pd
import numpy as np
import streamlit as st
import pickle
import joblib

with open("model73.pkl", "rb") as file_1:
    model1 = joblib.load(file_1)
# model = pickle.load(open("model.pkl", "rb"))
st.title("Water Quality Prediction")
ph = st.slider("PH", 0, 14)
chloramines = st.slider("Chloramines", 0, 15)
solids = st.slider("Solids", 100, 1000)
Hardness = st.number_input("Hardness")
Sulfate = st.number_input("Sulfate")
Conductivity = st.number_input("Conductivity")
Organic_Carbon = st.number_input("Organic_Carbon")
Trihalomethanes = st.number_input("Trihalomethanes")
Turbidity = st.number_input("Turbidity")
new_data = pd.DataFrame(
    {
        "ph": [ph],
        "Hardness": [Hardness],
        "Solids": [solids],
        "Chloramines": [chloramines],
        "Sulfate": [Sulfate],
        "Conductivity": [Conductivity],
        "Organic_carbon": [Organic_Carbon],
        "Trihalomethanes": [Trihalomethanes],
        "Turbidity": [Turbidity],
    }
)
if st.button("Predict"):
    final_pred = model1.predict(new_data)
    st.write("Result: ")
    if final_pred == 1:
        st.subheader("Potable")
    else:
        st.subheader("Non-Potable for Drinking")
