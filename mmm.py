import streamlit as st
from transformers import pipeline

# Title
st.title("text classification App")

# Load the classification pipeline with the specified model
classifier = pipeline('text-classification', model='Ammar-alhaj-ali/arabic-MARBERT-sentiment')


sentence = st.text_input("انا احبك", "انا احبك")
result = classifier(sentence)

st.write(result)
