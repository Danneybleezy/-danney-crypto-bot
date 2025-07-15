import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def ai_summarize(prompt):
    """Summarize news, facts, or market updates using Groq."""
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": "You are a witty and helpful crypto assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.8
    }

    try:
        res = requests.post(GROQ_API_URL, headers=headers, json=payload)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("❌ AI Summarize Error:", e)
        return "Crypto is moving fast today! Stay tuned. 🚀"

def ai_generate(prompt):
    """Generate original motivational or slang-based content with hashtags."""
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": "You're a social media manager creating unique, punchy, crypto-related content with emoji and hashtags."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.9
    }

    try:
        res = requests.post(GROQ_API_URL, headers=headers, json=payload)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("❌ AI Generate Error:", e)
        return "We're bullish on the future 🚀 Stay tuned! #Crypto"
