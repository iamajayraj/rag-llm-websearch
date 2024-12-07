
import streamlit as st
import requests

st.title("LLM-based RAG Search")

# Input for user query
query = st.text_input("Enter your query:")

if st.button("Search"):
    # Make a POST request to the Flask API
    url = "http://localhost:5001/query"
    response = requests.post(url,json={'query':query}) 

    # implement the flask call here
    
    if response:
        st.markdown(response.json()['answer'])
        
    else:
        #st.error(f"Error: {response.status_code}")
        st.error(f"Flask API Error: {response.status_code}")
