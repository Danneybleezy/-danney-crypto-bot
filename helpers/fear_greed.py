# helpers/fear_greed.py

import requests

def get_fear_greed_index():
    try:
        url = "https://api.alternative.me/fng/?limit=1"
        response = requests.get(url)
        data = response.json()

        value = data["data"][0]["value"]
        value_text = data["data"][0]["value_classification"]
        updated = data["data"][0]["timestamp"]

        message = f"😬 *Fear & Greed Index:* {value} – {value_text}\nStay sharp out there."

        return message

    except Exception as e:
        return f"⚠️ Couldn't fetch Fear & Greed Index: {e}"
