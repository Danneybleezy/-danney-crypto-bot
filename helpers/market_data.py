# helpers/market_data.py

import requests

def get_market_summary():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        btc = data.get("bitcoin", {})
        eth = data.get("ethereum", {})

        btc_price = btc.get("usd")
        btc_change = btc.get("usd_24h_change", 0)
        eth_price = eth.get("usd")
        eth_change = eth.get("usd_24h_change", 0)

        return (
            f"🪙 Market Update:\n"
            f"• BTC: ${btc_price:,.2f} ({btc_change:+.2f}%)\n"
            f"• ETH: ${eth_price:,.2f} ({eth_change:+.2f}%)"
        )
    except Exception as e:
        return f"⚠️ Error fetching market data: {e}"
