import os
import tweepy

# Authenticate using environment secrets
client = tweepy.Client(
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_SECRET"]
)

def post_to_twitter(text):
    try:
        response = client.create_tweet(text=text)
        tweet_id = response.data.get("id")
        print(f"✅ Tweet posted: https://twitter.com/user/status/{tweet_id}")
    except Exception as e:
        print(f"❌ Failed to post tweet: {e}")
