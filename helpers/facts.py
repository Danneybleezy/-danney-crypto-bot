import json
import random
from helpers.twitter import post_to_twitter
from helpers.groq_client import ai_summarize

def run_facts_mode():
    with open("data/crypto_facts.json") as f:
        facts = json.load(f)

    raw_fact = random.choice(facts)

    prompt = f"""Turn this crypto fact into a fun and slightly educational tweet. Be brief (2-4 lines), engaging, and end with emojis or a hashtag.

Fact: {raw_fact}
"""

    tweet = ai_summarize(prompt)
    post_to_twitter(tweet)
