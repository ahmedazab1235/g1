import streamlit as st
from transformers import pipeline

# Title
st.title("text classification App")

# Load the classification pipeline with the specified model
classifier = pipeline("text-classification", model="yangheng/deberta-v3-base-absa-v1.1")


sentence = st.text_input("", " love this product!")
result = classifier(sentence)

st.write(result)
