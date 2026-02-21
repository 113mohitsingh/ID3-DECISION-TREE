import streamlit as st
import pandas as pd

st.title("Play Tennis - Decision Tree")

# Dataset
data = {
    "Outlook": ["Sunny", "Sunny", "Overcast", "Rain", "Rain",
                "Rain", "Overcast", "Sunny", "Sunny", "Rain"],
    "Humidity": ["High", "High", "High", "High", "Normal",
                 "Normal", "Normal", "High", "Normal", "High"],
    "PlayTennis": ["No", "No", "Yes", "Yes", "Yes",
                   "No", "Yes", "No", "Yes", "Yes"]
}

df = pd.DataFrame(data)

st.subheader("Dataset")
st.write(df)

st.subheader("Predict PlayTennis")

outlook = st.selectbox("Select Outlook", ["Sunny", "Overcast", "Rain"])
humidity = st.selectbox("Select Humidity", ["High", "Normal"])

if st.button("Check Result"):

    # Simple Decision Tree Logic
    if outlook == "Overcast":
        result = "Yes"
    elif outlook == "Rain" and humidity == "High":
        result = "Yes"
    elif outlook == "Rain" and humidity == "Normal":
        result = "No"
    elif outlook == "Sunny" and humidity == "High":
        result = "No"
    else:
        result = "Yes"

    st.write("### Prediction Result:")
    st.write("PlayTennis =", result)
