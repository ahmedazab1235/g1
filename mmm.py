import streamlit as st
from transformers import pipeline

# Title
st.title("text classification App")

# Load the classification pipeline with the specified model
pipe = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")

sentence = st.text_input("I love this product! It's amazing and works perfectly.", "")
result = pipe(sentence)

if st.button("Submit"):
    st.write(result[0]['label'])
    st.write(result[0]['score'])
