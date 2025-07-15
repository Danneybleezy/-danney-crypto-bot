import feedparser
import random
from helpers.twitter import post_to_twitter
from helpers.groq_client import ai_summarize

COINDESK_RSS_URL = "https://www.coindesk.com/arc/outboundfeeds/rss/"

def fetch_latest_news():
    feed = feedparser.parse(COINDESK_RSS_URL)
    if not feed.entries:
        print("⚠️ No news entries found in RSS feed.")
        return None
    top_articles = feed.entries[:5]
    random_article = random.choice(top_articles)
    title = random_article.title
    link = random_article.link
    return f"{title} — {link}"

def run_crypto_news_mode():
    print("🗞️ Fetching latest crypto news from RSS...")
    news_headline = fetch_latest_news()

    if not news_headline:
        print("⚠️ No news headline fetched.")
        return

    prompt = f"Summarize this crypto news for Twitter in a casual tone with 3-5 lines, emojis, and relevant hashtags:\n\n{news_headline}"
    ai_tweet = ai_summarize(prompt)

    print("🧠 Tweeting summary:")
    print(ai_tweet)

    post_to_twitter(ai_tweet)
