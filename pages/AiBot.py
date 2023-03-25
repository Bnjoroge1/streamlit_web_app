import requests
import streamlit as st

url = "https://you-chat-gpt.p.rapidapi.com/"

st.title("Ai in your Service")
query = st.text_area("Ask me anything👇")
response_btn = st.button("Get Response")
if response_btn:
    payload = {
        "question": query,
        "max_response_time": 20
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "92e0b3f2b4msh3c165a5b3bb5840p12dc96jsn4368636b3287",
        "X-RapidAPI-Host": "you-chat-gpt.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    answer = response.json()
    st.info(answer["answer"])