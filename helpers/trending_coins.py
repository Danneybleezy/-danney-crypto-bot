# helpers/trending_coins.py

import requests

def get_trending_coins():
    try:
        url = "https://api.coingecko.com/api/v3/search/trending"
        response = requests.get(url, timeout=10)
        data = response.json()

        trending = data["coins"]
        top = trending[:5]  # Get top 5

        coin_list = [coin["item"]["name"] for coin in top]
        coins_text = ", ".join(coin_list)

        return f"📊 Trending Coins (Now): {coins_text}"
    except Exception as e:
        return f"⚠️ Error fetching trending coins: {e}"
