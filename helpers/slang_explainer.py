# helpers/slang_explainer.py

import json
import random
from groq_client import ai_summarize

def load_slang():
    with open("data/crypto_slang.json", "r", encoding="utf-8") as f:
        slang = json.load(f)
    return slang

def get_random_slang_explainer():
    slang_terms = load_slang()
    term = random.choice(list(slang_terms.keys()))
    definition = slang_terms[term]

    prompt = (
        f"Explain this crypto slang in a tweet-style format with emoji and fun tone. "
        f"Start with the slang word:\n\n"
        f"{term}: {definition}"
    )

    return ai_summarize(prompt)
