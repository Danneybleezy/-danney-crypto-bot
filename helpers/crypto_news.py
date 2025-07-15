# helpers/crypto_news.py

import requests
from groq_client import ai_summarize

def fetch_latest_crypto_news():
    url = "https://cryptopanic.com/api/v1/posts/?auth_token=demo&public=true"
    try:
        response = requests.get(url)
        data = response.json()
        headlines = [post["title"] for post in data.get("results", [])[:5]]
        return headlines
    except Exception as e:
        print(f"❌ Failed to fetch crypto news: {e}")
        return []

def summarize_news(headlines):
    if not headlines:
        return None

    text = "\n".join(f"- {h}" for h in headlines)
    prompt = (
        f"Summarize this crypto news in a motivational tweet style (English, max 4 lines). "
        f"Be clear, confident, and informal. Add a short comment:\n{text}"
    )
    return ai_summarize(prompt)
