import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def ai_generate_tweet(prompt):
    if not GROQ_API_KEY:
        raise Exception("Missing GROQ_API_KEY")

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": "You are a smart social media assistant that writes motivational, informative, and engaging tweets."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.8
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error generating tweet: {e}"
