import os
import streamlit as st
import requests

def generate_llama_explanation(crop_count, weed_count, decision):
    api_key = st.secrets["GROQ_API_KEY"]

    if not api_key:
        return "Δεν βρέθηκε REMOVED_GROQ_API_KEY στο περιβάλλον."

    prompt = f"""
You are an agricultural AI assistant.

A YOLOv8 model analyzed a field image.
Detected crops: {crop_count}
Detected weed regions: {weed_count}
System decision: {decision}

Explain this decision in simple language for a farmer.
Keep it short and practical.
"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Σφάλμα LLaMA: {response.status_code} - {response.text}"