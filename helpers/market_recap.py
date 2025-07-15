import requests
from helpers.groq_client import ai_summarize
from helpers.twitter import post_to_twitter

def run_market_recap_mode():
    try:
        # Fetch BTC and ETH prices
        coingecko = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin,ethereum",
            "vs_currencies": "usd",
            "include_24hr_change": "true"
        }
        price_data = requests.get(coingecko, params=params).json()

        btc = price_data["bitcoin"]
        eth = price_data["ethereum"]

        # Fetch top 3 gainers
        market_url = "https://api.coingecko.com/api/v3/coins/markets"
        top_params = {
            "vs_currency": "usd",
            "order": "percent_change_24h",
            "per_page": 5,
            "page": 1,
            "price_change_percentage": "24h"
        }
        top_coins = requests.get(market_url, params=top_params).json()

        gainers = [
            f"{coin['name']} ({coin['symbol'].upper()}) +{coin['price_change_percentage_24h']:.2f}%"
            for coin in top_coins[:3]
        ]

        recap_prompt = f"""
Summarize this daily crypto market recap in a tweet (with a positive tone, include emojis and hashtags):

BTC: ${btc['usd']:,} ({btc['usd_24h_change']:.2f}%)
ETH: ${eth['usd']:,} ({eth['usd_24h_change']:.2f}%)
Top Gainers: {', '.join(gainers)}
"""

        tweet = ai_summarize(recap_prompt)
        post_to_twitter(tweet)

    except Exception as e:
        print(f"❌ Failed to run market recap mode: {e}")
