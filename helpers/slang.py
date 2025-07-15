import json
import random
from helpers.twitter import post_to_twitter
from helpers.groq_client import ai_summarize

def run_slang_mode():
    with open("data/crypto_slang.json") as f:
        slang_data = json.load(f)

    slang_term, definition = random.choice(list(slang_data.items()))

    prompt = f"""Explain this crypto slang like you're talking to a beginner on Twitter in a fun and engaging way. Be short and witty.

Slang: {slang_term}
Meaning: {definition}

End the tweet with 1-2 relevant emojis and a hashtag like #CryptoSlang.
"""

    tweet = ai_summarize(prompt)
    post_to_twitter(tweet)
