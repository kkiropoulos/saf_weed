import streamlit as st
import requests
import os

st.header("🤖 Συνομιλία με το LLaMA")

# Αρχικοποίηση session state για το ιστορικό
if "messages" not in st.session_state:
    st.session_state.messages = []

api_key = st.secrets["GROQ_API_KEY"]
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

# Εμφάνιση ιστορικού συνομιλίας
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Πεδίο εισαγωγής μηνύματος
if prompt := st.chat_input("Πληκτρολόγησε το μήνυμά σου..."):
    # Εμφάνιση του μηνύματος του χρήστη
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Δημιουργία payload με όλο το ιστορικό της συνομιλίας
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": st.session_state.messages
    }

    # Αποστολή αιτήματος στο API
    with st.spinner("Το LLaMA απαντά..."):
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)

    # Εμφάνιση απάντησης
    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        st.chat_message("assistant").markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
    else:
        st.error(f"⚠️ Σφάλμα: {response.status_code}")
        st.text(response.text)