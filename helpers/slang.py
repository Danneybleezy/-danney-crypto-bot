import json
import random
from helpers.groq_client import ai_summarize
from helpers.twitter import post_to_twitter

def run_slang_mode():
    with open("data/crypto_slang.json") as f:
        slang_data = json.load(f)

    slang = random.choice(slang_data)
    term = slang["term"]
    definition = slang["definition"]

    # Prompt to enhance it for Twitter
    prompt = f"""
Make this slang tweet-worthy in 3-4 lines, fun and easy to understand:

Term: {term}
Meaning: {definition}

Include 2 crypto-related hashtags and 1 emoji.
Language: English or Pidgin.
"""

    tweet = ai_summarize(prompt)
    post_to_twitter(tweet)
