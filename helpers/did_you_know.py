# helpers/did_you_know.py

import json
import random
from groq_client import ai_summarize

def load_facts():
    with open("data/crypto_facts.json", "r", encoding="utf-8") as f:
        facts = json.load(f)
    return facts

def get_random_fact():
    facts = load_facts()
    fact = random.choice(facts)
    prompt = (
        f"Turn this crypto fact into a tweet-style 'Did You Know?' in 3-4 lines with an emoji and human tone:\n"
        f"{fact}"
    )
    return ai_summarize(prompt)
