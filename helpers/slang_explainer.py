# helpers/slang_explainer.py

import json
import random

def get_crypto_slang():
    try:
        with open("data/crypto_slang.json") as f:
            slang_data = json.load(f)

        term = random.choice(list(slang_data.keys()))
        meaning = slang_data[term]

        return f"🧠 CRYPTO SLANG:\n\n{term}: {meaning}"
    except Exception as e:
        return f"⚠️ Error loading slang: {e}"
