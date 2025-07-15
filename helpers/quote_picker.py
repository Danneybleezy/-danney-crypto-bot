# helpers/quote_picker.py

import json
import random
from helpers.ai_generate import generate_tweet

def get_crypto_quote():
    try:
        with open("data/crypto_quotes.json") as f:
            quotes = json.load(f)

        quote = random.choice(quotes)
        quote_text = f"\"{quote['text']}\" – {quote['author']}"

        prompt = f"""
You are a crypto-savvy motivational speaker. 
Take this quote and write a short, thoughtful tweet explaining why it’s powerful in today's crypto world.
Include the quote. Make it human, use slang or emoji sparingly but naturally.

QUOTE: {quote_text}
"""

        ai_response = generate_tweet(prompt)
        return ai_response.strip()

    except Exception as e:
        return f"⚠️ Error loading quote: {e}"
