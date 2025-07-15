# main.py

import random
from helpers.bot_modes import (
    generate_motivational_tweet,
    generate_did_you_know,
    generate_crypto_slang,
    generate_market_recap,
    generate_trending_coins,
    generate_crypto_news
)
from helpers.quote_picker import get_crypto_quote
from helpers.fear_greed import get_fear_greed_index
from helpers.bot import post_tweet

modes = [
    generate_motivational_tweet,
    generate_crypto_news,
    generate_market_recap,
    generate_trending_coins,
    generate_did_you_know,
    generate_crypto_slang,
    get_crypto_quote,
    get_fear_greed_index
]

def main():
    print("🚀 Selecting random content mode...")
    mode = random.choice(modes)

    try:
        tweet = mode()
        post_tweet(tweet)
    except Exception as e:
        print("❌ Bot failed:", e)

if __name__ == "__main__":
    main()
