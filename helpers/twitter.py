import os
import tweepy

# Load Twitter API credentials from environment variables
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_SECRET
)

api = tweepy.API(auth)

def post_to_twitter(tweet_text):
    print("📢 Attempting to tweet:\n", tweet_text)

    try:
        api.update_status(tweet_text)
        print("✅ Tweet posted successfully!")
    except tweepy.errors.Forbidden as e:
        print("❌ Failed to post tweet: Forbidden –", e)
        if "duplicate" in str(e).lower():
            print("⚠️ This tweet appears to be a duplicate.")
    except Exception as e:
        print("❌ Unexpected error posting tweet:", e)
