import streamlit as st
import requests
st.title("My Web App")
url = "https://gpt-based-google-search.p.rapidapi.com/search"

st.title("GPT-based Google Search ")
query = st.text_input("Enter your query to search👇")
search_btn = st.button("Search")
if search_btn:
    payload = {"question": query}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "92e0b3f2b4msh3c165a5b3bb5840p12dc96jsn4368636b3287",
        "X-RapidAPI-Host": "gpt-based-google-search.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    content = response.json()
    answer = content["data"]
    st.info(answer)
