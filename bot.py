# bot.py

import os
from datetime import datetime
from bot_modes import get_random_tweet
import tweepy

# 🐦 Authenticate Twitter
client = tweepy.Client(
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_SECRET"]
)

def run_bot():
    tweet = get_random_tweet()
    try:
        response = client.create_tweet(text=tweet)
        tweet_id = response.data.get("id")
        print(f"✅ Tweet posted: https://twitter.com/user/status/{tweet_id}")
    except Exception as e:
        print(f"❌ Failed to post tweet: {e}")
        print(f"Tried tweet: {tweet}")

if __name__ == "__main__":
    now = datetime.utcnow()
    print(f"🕒 Bot running at {now.isoformat()} UTC")
    run_bot()
