import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def ai_summarize(prompt: str) -> str:
    return _ask_groq(
        system_prompt="You are a witty and helpful crypto assistant.",
        user_prompt=prompt
    )

def ai_generate(prompt: str) -> str:
    return _ask_groq(
        system_prompt="You are a creative assistant that writes engaging, motivating, and informative tweets about crypto.",
        user_prompt=prompt
    )

def _ask_groq(system_prompt: str, user_prompt: str) -> str:
    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.8
    }

    try:
        res = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("❌ AI Generation Error:", e)
        return "Stay tuned. 🚀"
