import streamlit as st
from backend_cipher import encrypt, decrypt

st.title("Caesar Cipher")
st.subheader("Encrypt And Decrypt The Text")
key = st.number_input("Select Key", min_value=1, max_value=26, value=3)
text = st.text_area("Enter Text")
col1, col2 = st.columns(2)
with col1:
    encrypt_btn = st.button("Encrypt")
with col2:
    decrypt_btn = st.button("Decrypt")
if encrypt_btn:
    st.subheader("Encrypted Text")
    st.info(encrypt(text, key))
elif decrypt_btn:
    st.subheader("Decrypted Text")
    st.info(decrypt(text, key))
