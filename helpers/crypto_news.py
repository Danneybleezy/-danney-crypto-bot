import random
import feedparser
from helpers.twitter import post_to_twitter
from helpers.groq_client import ai_summarize

def run_crypto_news_mode():
    print("🤖 Running bot mode: run_crypto_news_mode")
    print("🗞️ Fetching latest crypto news from RSS...")

    rss_urls = [
        "https://www.coindesk.com/arc/outboundfeeds/rss/",
        "https://cointelegraph.com/rss",
        "https://cryptoslate.com/feed/"
    ]

    try:
        rss_url = random.choice(rss_urls)
        feed = feedparser.parse(rss_url)

        print(f"🔗 RSS Source: {rss_url}")
        print("🔍 Raw feed entries:", len(feed.entries))

        if not feed.entries:
            print("⚠️ No news entries found in RSS feed.")
            post_to_twitter("🚨 Crypto is quiet right now. Stay sharp and keep building. #CryptoNews")
            return

        latest_entry = feed.entries[0]
        headline = latest_entry.get("title", "Latest crypto update")
        summary = latest_entry.get("summary", "")
        link = latest_entry.get("link", "")

        prompt = f"""Summarize this crypto news headline in a casual tone with emojis and 2 hashtags:
        Title: {headline}
        Summary: {summary}
        Link: {link}
        """

        tweet = ai_summarize(prompt)
        if link:
            tweet += f"\n\n🔗 {link}"

        post_to_twitter(tweet)

    except Exception as e:
        print("❌ Failed to fetch news:", str(e))
        post_to_twitter("⚠️ Couldn't fetch crypto news right now. Stay tuned. #CryptoUpdate")
