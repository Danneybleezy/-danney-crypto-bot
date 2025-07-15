import requests
from helpers.twitter import post_to_twitter

def run_fear_greed_mode():
    try:
        response = requests.get("https://api.alternative.me/fng/")
        data = response.json()["data"][0]

        index_value = data["value"]
        index_text = data["value_classification"]
        updated_at = data["timestamp"]

        emojis = {
            "Extreme Fear": "😱",
            "Fear": "😨",
            "Neutral": "😐",
            "Greed": "😎",
            "Extreme Greed": "🚀"
        }

        emoji = emojis.get(index_text, "📊")

        tweet = (
            f"🧠 *Fear & Greed Index Update*\n\n"
            f"Market Sentiment: {index_text} {emoji}\n"
            f"Index Score: {index_value}/100\n"
            f"#Crypto #Bitcoin #Sentiment"
        )

        post_to_twitter(tweet)

    except Exception as e:
        print("❌ Error fetching Fear & Greed Index:", e)
