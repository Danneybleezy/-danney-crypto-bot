import json
import random
from helpers.groq_client import ai_generate
from helpers.twitter import post_to_twitter

def run_slang_mode():
    with open("data/crypto_slang.json") as f:
        slang_data = json.load(f)

    slang_entry = random.choice(slang_data)
    slang_term = slang_entry["term"]

    prompt = (
        f"Write a unique, cool 3–5 line tweet explaining the crypto slang: '{slang_term}'. "
        "Make it fun, relatable, and clear to beginners. Use informal tone, include emojis, "
        "and add 2–4 relevant crypto hashtags at the end (like #Crypto, #Blockchain, #Web3)."
    )

    tweet = ai_generate(prompt)
    post_to_twitter(tweet)
