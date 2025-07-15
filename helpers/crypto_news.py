import requests
import random
from groq_client import ai_summarize
from helpers.twitter import post_to_twitter

# ✅ Updated with your CryptoPanic API key
CRYPTO_NEWS_API = "https://cryptopanic.com/api/v1/posts/?auth_token=74cd1d21dd88cb06621b8da8a9fb32c7f9449699&public=true"

def fetch_latest_crypto_news():
    response = requests.get(CRYPTO_NEWS_API)
    if response.status_code != 200:
        print("❌ Failed to fetch news:", response.text)
        return []

    data = response.json()
    posts = data.get("results", [])
    headlines = [post["title"] for post in posts if post.get("title")]

    return headlines[:5]  # Limit to 5 latest news headlines

def run_crypto_news_mode():
    print("🗞️ Fetching latest crypto news...")
    headlines = fetch_latest_crypto_news()

    if not headlines:
        print("⚠️ No news headlines fetched.")
        return

    # Join headlines and summarize with Groq
    text_block = "\n".join(f"- {h}" for h in headlines)
    prompt = f"""Summarize the following crypto news headlines into a short tweet that sounds smart and engaging:

{text_block}

Add relevant hashtags like #Bitcoin, #Crypto, or #Web3.
"""
    summary = ai_summarize(prompt)

    tweet = summary.strip()
    if tweet:
        post_to_twitter(tweet)
    else:
        print("⚠️ Groq returned empty summary.")
