# helpers/fear_greed.py

import requests

def get_fear_greed_index():
    try:
        url = "https://api.alternative.me/fng/"
        response = requests.get(url, timeout=10)
        data = response.json()

        index = data["data"][0]
        value = index["value"]
        value_classification = index["value_classification"]
        timestamp = index["timestamp"]

        return f"📉 Fear & Greed Index: {value} ({value_classification})"
    except Exception as e:
        return f"⚠️ Error fetching Fear & Greed Index: {e}"
