"""
Quick API Key Test - Moon Dev
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from api import MoonDevAPI

def main():
    api = MoonDevAPI()

    print("🌙 Moon Dev API Key Test")
    print("=" * 40)

    if not api.api_key:
        print("❌ No API key found in .env")
        return

    print(f"✅ API Key loaded: {api.api_key[:10]}...")
    print()

    # Test 1: Liquidation stats
    print("Testing /api/liquidations/stats.json...")
    try:
        stats = api.get_liquidation_stats()
        total = stats.get('total_value_usd', 0)
        count = stats.get('total_count', 0)
        print(f"  ✅ Liquidations: ${total:,.0f} ({count} events)")
    except Exception as e:
        print(f"  ❌ Liquidations failed: {e}")

    # Test 2: Prices
    print("\nTesting /api/prices...")
    try:
        prices = api.get_prices()
        btc = prices.get('prices', {}).get('BTC', 'N/A')
        eth = prices.get('prices', {}).get('ETH', 'N/A')
        print(f"  ✅ BTC: ${float(btc):,.0f} | ETH: ${float(eth):,.0f}")
    except Exception as e:
        print(f"  ❌ Prices failed: {e}")

    # Test 3: HLP Sentiment
    print("\nTesting /api/hlp/sentiment...")
    try:
        sentiment = api.get_hlp_sentiment()
        zscore = sentiment.get('z_score', 0)
        sig = sentiment.get('signal', {})
        direction = sig.get('direction', 'N/A') if isinstance(sig, dict) else sig
        print(f"  ✅ Z-Score: {zscore:.2f} | Signal: {direction}")
    except Exception as e:
        print(f"  ❌ HLP Sentiment failed: {e}")

    print()
    print("=" * 40)
    print("🌙 API Key test complete!")

if __name__ == "__main__":
    main()
