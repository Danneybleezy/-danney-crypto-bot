import json
import random
from helpers.twitter import post_to_twitter
from helpers.groq_client import ai_summarize

def run_quote_mode():
    with open("data/crypto_quotes.json") as f:
        quotes = json.load(f)

    raw_quote = random.choice(quotes)

    prompt = f"""Take this crypto quote and turn it into a motivational tweet. Add 1–2 emojis, and keep it in 3–5 lines max.

Quote: {raw_quote}
"""

    tweet = ai_summarize(prompt)
    post_to_twitter(tweet)
