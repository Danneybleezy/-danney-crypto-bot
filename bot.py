# bot.py

import os
import json
from datetime import datetime
from ai_generate import ai_generate_motivation
import tweepy

# Load config
with open("config.json") as f:
    config = json.load(f)

# Authenticate with Twitter API (v2 with OAuth 1.0a)
client = tweepy.Client(
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_SECRET"]
)

def run_bot():
    tweet_text = ai_generate_motivation()
    print("📢 AI Tweet:", tweet_text)
    try:
        response = client.create_tweet(text=tweet_text)
        tweet_id = response.data.get("id")
        print(f"✅ Tweet posted: https://twitter.com/user/status/{tweet_id}")
    except Exception as e:
        print(f"❌ Failed to post tweet: {e}")

if __name__ == "__main__":
    now = datetime.utcnow()
    print(f"🕒 Posting tweet at: {now.isoformat()} UTC")
    run_bot()
