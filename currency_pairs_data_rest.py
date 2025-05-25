""" Here are some of the most commonly traded currency pairs:

EUR/USD (Euro and US dollar): Known as "Fiber", it is the most traded pair, representing the world's two largest economies.
USD/JPY (US dollar and Japanese yen): Known as "Gopher", it is the second most traded pair, reflecting the high liquidity of the yen in Asia and the dollar globally.
GBP/USD (British pound and US dollar): Known as "Cable", it reflects the economic ties between the UK and the US.
USD/CHF (US dollar and Swiss franc): Known as "Swissie", it is influenced by the stability and neutrality of the Swiss economy.
AUD/USD (Australian dollar and US dollar): Known as "Aussie", it is tied closely to Australia's export commodities.
USD/CAD (US dollar and Canadian dollar): Known as "Loonie", it reflects Canada's economy and its commodity exports.
NZD/USD (New Zealand dollar and US dollar): Known as "Kiwi", it is less traded but reflects New Zealand's economy.
GBP/EUR (British pound and euro): Known as "Chunnel", it reflects the economic relationship between the UK and the eurozone.
EUR/JPY (Euro and Japanese yen): Known as "Yuppy", it is influenced by the volume of yen carry trades and market sentiment.
EUR/CHF (Euro and Swiss franc): Known as "Euro-swissie", it reflects the close economic relationship between Switzerland and the eurozone. """


import tradermade as tm

def get_live_data(api_key, currencies, fields=None):
    """
    Fetch live forex data for the specified currencies and fields.

    :param api_key: TraderMade REST API key
    :param currencies: Comma-separated string of currency pairs (e.g., 'EURUSD,GBPUSD')
    :param fields: List of fields to fetch (e.g., ['bid', 'mid', 'ask'])
    :return: Live forex data or an error message
    """
    try:
        # Set the API key
        tm.set_rest_api_key(api_key)

        # Fetch live data
        live_data = tm.live(currency=currencies, fields=fields)
        return live_data
    except Exception as e:
        return f"Error fetching live data: {e}"

if __name__ == "__main__":
    # Replace with your actual valid API key
    API_KEY = "Your Key"
    CURRENCY_PAIRS = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", 
                      "USDCHF", "USDCAD", "NZDUSD", "EURJPY", 
                      "EURCHF", "GBPCHF", "GBPJPY"]
    FIELDS = ["bid", "mid", "ask"]

    # Process each currency pair
    for pair in CURRENCY_PAIRS:
        print(f"Processing currency pair: {pair}")
        live_data = get_live_data(API_KEY, pair, FIELDS)
        print(f"Data for {pair}:")
        print(live_data)
        #live_data = get_live_data(API_KEY, pair, FIELDS)
        #print(live_data)
        print()

    print("Processing of currency pairs done.")
