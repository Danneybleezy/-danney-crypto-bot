# bot.py

import os
import time
import random
from datetime import datetime
from ai_generate import ai_generate_motivation
import tweepy
import json

# Debug: show env keys if needed
# print("ENV keys →", list(os.environ.keys()))

# Load config
with open("config.json") as f:
    config = json.load(f)

keywords = config["keywords"]
interval_range = config["tweet_interval_hours_range"]

# Authenticate
client = tweepy.Client(
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_SECRET"]
)

def run_bot():
    tweet = generate_motivation()
    try:
        response = client.create_tweet(text=tweet)
        tweet_id = response.data.get("id")
        print(f"✅ Tweeted successfully: https://twitter.com/user/status/{tweet_id}")
    except Exception as e:
        print(f"❌ Tweet failed: {e}")

if __name__ == "__main__":
    now = datetime.utcnow().isoformat()
    print(f"🕒 Posting at: {now} UTC")
    run_bot()
