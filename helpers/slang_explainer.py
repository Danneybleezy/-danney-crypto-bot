# helpers/slang_explainer.py

import json
import random
from groq_client import ai_summarize

def load_slang():
    with open("data/crypto_slang.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_crypto_slang_tweet():
    slang_data = load_slang()
    entry = random.choice(slang_data)

    term = entry.get("term")
    meaning = entry.get("meaning")

    prompt = (
        f"Write a tweet that explains the crypto slang '{term}'.\n"
        f"Make it fun, informal, 2–4 lines. Use Gen Z or crypto street style. You can include an emoji and hashtag.\n\n"
        f"Meaning: {meaning}"
    )

    return ai_summarize(prompt)
