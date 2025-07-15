# helpers/greed_index.py

import requests

def get_fear_and_greed_index():
    url = "https://api.alternative.me/fng/"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if "data" in data and len(data["data"]) > 0:
            index_data = data["data"][0]
            value = index_data["value"]
            value_classification = index_data["value_classification"]
            return f"📊 Crypto Fear & Greed Index: {value} ({value_classification})"
        else:
            return "❌ Unable to fetch Fear & Greed Index"
    except Exception as e:
        return f"⚠️ Error fetching index: {e}"
