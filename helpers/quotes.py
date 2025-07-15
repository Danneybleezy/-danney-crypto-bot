import random
from helpers.groq_client import ai_summarize
from helpers.twitter import post_to_twitter
import json

def run_quote_mode():
    with open("data/crypto_quotes.json") as f:
        quotes = json.load(f)

    quote = random.choice(quotes)

    prompt = f"""
    Take this quote and rewrite it to be more motivational, slightly longer, and engaging for Twitter. Add a relevant hashtag or emoji. Don’t change the meaning:

    "{quote}"
    """

    tweet = ai_summarize(prompt)
    post_to_twitter(tweet)
