import random
import json
from helpers.groq_client import ai_summarize
from helpers.twitter import post_to_twitter

def load_facts():
    with open("data/crypto_facts.json") as f:
        return json.load(f)

def rewrite_fact_with_ai(fact):
    prompt = (
        f"Rewrite this crypto fact in 3–5 short tweet-friendly lines. "
        f"Add a surprising or clever tone. Add emojis and 1–2 hashtags:\n\n"
        f"Fact: {fact}"
    )
    return ai_summarize(prompt)

def run_facts_mode():
    all_facts = load_facts()
    random_fact = random.choice(all_facts)
    tweet = rewrite_fact_with_ai(random_fact)
    post_to_twitter(tweet)
