import streamlit as st
import requests

url = f'https://app.plaraphy.com/api/rewriter'
st.title("Paraphraser")
paragraph = st.text_area("Enter Here to paraphrase👇: ")
paraphrase = st.button("Paraphrase")
if paraphrase:
	payload = f'text={paragraph}.&mode=fluent&lang=es&unique=true'
	headers = {
		'accept': 'application/json',
		'content-type': 'application/x-www-form-urlencoded',
		'authorization': 'Bearer 24701|nL9k0AoCJvMobweYWR4WhCzdwE0DkAmfUNJXtC6u',
	}

	response = requests.request('POST', url, data=payload, headers=headers)

	print(response.text)
	content = response.json()
	paraphrased = content["rewrited"]
	st.info(paraphrased)

