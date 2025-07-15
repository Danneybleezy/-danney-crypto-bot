import random
from helpers.groq_client import ai_summarize
from helpers.twitter import post_to_twitter

def run_facts_mode():
    prompt_variants = [
        "Give me a never-before-seen fun crypto fact with emojis and relevant hashtags.",
        "Share an interesting and unique cryptocurrency fact. Include emojis and hashtags.",
        "Tell me a surprising blockchain or crypto fact to tweet, with hashtags.",
        "Write a fun fact about crypto that hasn’t been tweeted before. Add trending hashtags.",
        "Create a tweet-worthy crypto fact with unique phrasing, emojis, and hashtags."
    ]

    selected_prompt = random.choice(prompt_variants)

    print("🤖 Running bot mode: run_facts_mode")
    tweet = ai_summarize(selected_prompt)

    # Add a random emoji to ensure uniqueness
    emoji_suffix = random.choice(["✨", "🔥", "🚀", "💡", "🧠", "💰", "🌐", "🪙", "📈"])
    final_tweet = f"{tweet} {emoji_suffix}"

    post_to_twitter(final_tweet)
