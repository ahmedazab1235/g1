import streamlit as st
import pandas as pd

# Title
st.title("Hello World App")

st.write("This is a simple Streamlit app that displays a greeting message.")
age = st.slider("Select your age:", 0, 100, 25)


name = st.text_input("Enter your name:", "")

if st.button("Submit"):
    st.write(f"Hello, {name} ! You selected age: {age}")

df = pd.DataFrame({
    "Name": ["ahmed", "essam", "azab"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
})

st.dataframe(df)