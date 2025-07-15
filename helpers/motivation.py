from helpers.ai_generate import ai_generate_tweet

def run_motivation_mode():
    prompt = (
        "Write a motivational tweet about success, hustle, mindset, or growth. "
        "Make it 3–5 lines long, engaging, and end with relevant hashtags. Mix in a Nigerian or Pidgin English flavor if possible."
    )
    tweet = ai_generate_tweet(prompt)
    return tweet
