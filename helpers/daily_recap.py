# helpers/daily_recap.py

import requests

def fetch_market_summary():
    try:
        cg_data = requests.get("https://api.coingecko.com/api/v3/global").json()
        market_cap = cg_data["data"]["total_market_cap"]["usd"]
        btc_dominance = cg_data["data"]["market_cap_percentage"]["btc"]

        top_gainers_data = requests.get("https://api.coingecko.com/api/v3/coins/markets", params={
            "vs_currency": "usd",
            "order": "percent_change_24h_desc",
            "per_page": 3,
            "page": 1
        }).json()

        gainers = [f"{coin['name']} (+{coin['price_change_percentage_24h']:.2f}%)" for coin in top_gainers_data]

        nft_volume_data = requests.get("https://api.nftscan.com/api/v2/statistics/global/trend/volume", timeout=10).json()
        nft_volume = nft_volume_data.get("data", {}).get("volumes", [{}])[-1].get("volume", "N/A")

        defi_data = requests.get("https://api.llama.fi/summary/all", timeout=10).json()
        defi_tvl = defi_data.get("totalLiquidityUSD", "N/A")

        summary = (
            f"🌍 Market Recap:\n"
            f"- Total Cap: ${market_cap:,.0f}\n"
            f"- BTC Dominance: {btc_dominance:.2f}%\n"
            f"- Top Gainers: {', '.join(gainers)}\n"
            f"- NFT Volume (24h): ${nft_volume:,.0f}\n"
            f"- DeFi TVL: ${float(defi_tvl):,.0f} 🔐"
        )
        return summary
    except Exception as e:
        return f"⚠️ Error fetching market recap: {e}"
