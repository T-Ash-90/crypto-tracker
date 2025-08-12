import requests

def fetch_top_50_prices():
    # CoinGecko API URL for the top 50 cryptocurrencies
    url = "https://api.coingecko.com/api/v3/coins/markets"

    # Parameters to fetch the top 50 coins, sorted by market cap (descending)
    params = {
        "vs_currency": "eur",  # You can change this to USD, GBP, etc.
        "order": "market_cap_desc",  # Sort by market cap (descending)
        "per_page": 50,  # Limit to the top 50 coins
        "page": 1,  # The first page of results
    }

    # Send the request to the CoinGecko API
    response = requests.get(url, params=params)

    # Check if the response was successful (status code 200)
    if response.status_code == 200:
        data = response.json()

        # Print the name and price of each cryptocurrency
        for coin in data:
            name = coin['name']
            price = coin['current_price']
            print(f"{name}: €{price}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Call the function to fetch and display the prices
fetch_top_50_prices()
