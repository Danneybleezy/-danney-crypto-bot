# helpers/nft_defi_summary.py

import requests

def get_nft_volume_summary():
    try:
        response = requests.get("https://api.nftscan.com/api/v2/statistics/market/24h", timeout=10)
        data = response.json()["data"]
        volume = float(data["volume_usd"])
        tx_count = data["tx_count"]

        return f"🖼️ NFT 24h Volume: ${volume:,.0f} | Transactions: {tx_count}"
    except Exception as e:
        return f"⚠️ Error fetching NFT data: {e}"

def get_defi_tvl_summary():
    try:
        response = requests.get("https://api.llama.fi/tvl", timeout=10)
        data = response.json()
        tvl = data.get("tvl", 0)

        return f"🧪 DeFi TVL: ${tvl:,.0f}"
    except Exception as e:
        return f"⚠️ Error fetching DeFi data: {e}"
