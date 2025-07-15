import random
from helpers.bot_modes import (
    run_motivation_mode,
    run_crypto_news_mode,
    run_market_recap_mode,
    run_slang_mode,
    run_facts_mode,
    run_quote_mode,
    run_fear_greed_mode
)

# Randomly pick one bot mode per run
bot_modes = [
    run_motivation_mode,
    run_crypto_news_mode,
    run_market_recap_mode,
    run_slang_mode,
    run_facts_mode,
    run_quote_mode,
    run_fear_greed_mode
]

if __name__ == "__main__":
    selected_mode = random.choice(bot_modes)
    print(f"🤖 Running bot mode: {selected_mode.__name__}")
    selected_mode()
