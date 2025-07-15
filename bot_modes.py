# bot_modes.py

import random

from helpers.motivation_ai import get_motivational_tweet
from helpers.crypto_news import get_latest_crypto_news
from helpers.market_recap import get_market_recap
from helpers.slang_explainer import get_crypto_slang_tweet
from helpers.crypto_quotes import get_crypto_quote_tweet
from helpers.did_you_know import get_did_you_know_fact
from helpers.fear_greed import get_fear_greed_summary
from helpers.trending_coins import get_trending_coin_summary

def get_random_tweet():
    modes = [
        get_motivational_tweet,
        get_latest_crypto_news,
        get_market_recap,
        get_crypto_slang_tweet,
        get_crypto_quote_tweet,
        get_did_you_know_fact,
        get_fear_greed_summary,
        get_trending_coin_summary
    ]

    chosen = random.choice(modes)
    return chosen()
