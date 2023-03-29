import requests
import streamlit as st

url = "https://scodex-api.p.rapidapi.com/"

st.title("Ai in your Service")
query = st.text_area("Ask me anything👇")
response_btn = st.button("Get Response")

if response_btn:
    payload = {"prompt": query}
    headers = {
        "content-type": "application/json",
        "Content-Type": "application/json",
        "X-RapidAPI-Key": "92e0b3f2b4msh3c165a5b3bb5840p12dc96jsn4368636b3287",
        "X-RapidAPI-Host": "scodex-api.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    answer = response.json()
    st.info(answer["bot"])
