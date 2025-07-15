import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def ai_summarize(prompt):
    if not GROQ_API_KEY:
        raise Exception("Missing GROQ_API_KEY")

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": "You are a crypto expert that summarizes news in short, human-style tweets."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        res = requests.post(url, headers=headers, json=payload)
        return res.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error from Groq: {e}"
