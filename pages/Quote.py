import requests
import streamlit as st

st.title("A Random Quote")
btn = st.button("Get Quote")
if btn:
	URL = "https://api.quotable.io/random"
	response = requests.get(URL)
	content = response.json()
	quote = content["content"]
	author = content["author"]
	st.info(quote)
	st.subheader(f"A quote by {author}")