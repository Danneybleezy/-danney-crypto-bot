# news_fetcher.py

import feedparser
import random
import os
import requests

def fetch_crypto_news(limit=3):
    """Fetch top news items from CryptoPanic RSS feed"""
    rss_url = "https://cryptopanic.com/news/rss"
    feed = feedparser.parse(rss_url)
    entries = feed.entries[:limit]
    headlines = [entry.title for entry in entries]
    return headlines

def summarize_with_groq(headlines):
    """Summarize news using Groq API"""
    if not headlines:
        return "No crypto news found at the moment."

    prompt = "Summarize the following crypto news headlines in a friendly, tweetable tone. Add 1 emoji and keep it short:\n\n"
    prompt += "\n".join(f"- {h}" for h in headlines)

    groq_api_key = os.environ.get("GROQ_API_KEY")
    if not groq_api_key:
        return "❌ Groq API key not found."

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {groq_api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mixtral-8x7b-32768",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }
        )
        summary = response.json()["choices"][0]["message"]["content"]
        return summary.strip()
    except Exception as e:
        return f"❌ Failed to summarize: {e}"

def get_summarized_crypto_news():
    news = fetch_crypto_news()
    return summarize_with_groq(news)

if __name__ == "__main__":
    print("📰 Latest crypto summary:")
    print(get_summarized_crypto_news())
