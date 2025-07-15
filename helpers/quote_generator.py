# helpers/quote_generator.py

import json
import random
from groq_client import ai_summarize

def load_quotes():
    with open("data/crypto_quotes.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_motivational_quote():
    quotes = load_quotes()
    raw_quote = random.choice(quotes)

    prompt = (
        f"Turn this quote into a short motivational tweet (2–4 lines), add a powerful tone, include one or two emojis. "
        f"If you like, end with a related hashtag.\n\n"
        f"Quote: \"{raw_quote}\""
    )

    return ai_summarize(prompt)
