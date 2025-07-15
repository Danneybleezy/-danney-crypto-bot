# ai_generate.py

import os
import random
import json
import requests

with open("config.json") as f:
    config = json.load(f)

keywords = config["keywords"]
language_mix = config["language_mix"]
tone = config.get("tone", "motivational")

def ai_generate_motivation():
    topic = random.choice(keywords)
    lang = random.choices(["english", "pidgin"], weights=[
        language_mix.get("english", 0.8),
        language_mix.get("pidgin", 0.2)
    ])[0]

    style_note = "Use Nigerian Pidgin and add emojis." if lang == "pidgin" else "Use clear English with emojis."

    prompt = f"""Write a motivational tweet about "{topic}" in a {tone} tone. Keep it under 280 characters. {style_note} Add 1-2 relevant hashtags."""

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.environ['GROQ_API_KEY']}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mixtral-8x7b-32768",
            "messages": [
                {"role": "system", "content": "You are a motivational speaker who tweets like a wise Nigerian."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.9
        }
    )

    try:
        ai_text = response.json()["choices"][0]["message"]["content"]
        return ai_text.strip()
    except Exception as e:
        print("❌ AI failed to respond:", e)
        return f"Keep grinding. {topic} will pay off. 💯"
