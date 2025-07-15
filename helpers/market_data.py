# helpers/market_data.py

import requests

def get_market_summary():
    url = "https://api.coingecko.com/api/v3/global"
    try:
        res = requests.get(url).json()
        data = res["data"]

        btc_dom = data["market_cap_percentage"]["btc"]
        eth_dom = data["market_cap_percentage"]["eth"]
        active_cryptos = data["active_cryptocurrencies"]
        total_volume = data["total_volume"]["usd"] / 1e9
        market_cap = data["total_market_cap"]["usd"] / 1e12

        return {
            "btc_dom": round(btc_dom, 2),
            "eth_dom": round(eth_dom, 2),
            "active_cryptos": active_cryptos,
            "volume_b": round(total_volume, 2),
            "market_cap_t": round(market_cap, 2)
        }
    except Exception as e:
        print(f"❌ Error fetching market summary: {e}")
        return None

def get_top_gainers(limit=3):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "percent_change_24h",
        "per_page": 50,
        "page": 1,
        "sparkline": False
    }
    try:
        res = requests.get(url, params=params).json()
        gainers = sorted(res, key=lambda x: x["price_change_percentage_24h"] or 0, reverse=True)
        return gainers[:limit]
    except Exception as e:
        print(f"❌ Error fetching top gainers: {e}")
        return []
