import requests

# ANSI escape sequences for color
class TerminalColors:
    RESET = "\033[0m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    ORANGE = "\033[38;5;214m"  # Approximate Orange using 256-color palette
    WHITE = "\033[97m"

def fetch_top_50_prices():
    # CoinGecko API URL for the top 50 cryptocurrencies
    url = "https://api.coingecko.com/api/v3/coins/markets"

    # Parameters to fetch the top 50 coins, sorted by market cap (descending)
    params = {
        "vs_currency": "eur",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
    }

    try:
        # Send a GET request to the CoinGecko API with a timeout of 10 seconds
        response = requests.get(url, params=params, timeout=10)

        # Check if the response was successful (status code 200)
        if response.status_code == 200:
            try:
                # Try to parse the response as JSON
                data = response.json()

                # Print the name, price, and 24h price change of each cryptocurrency
                for coin in data:
                    name = coin['name']
                    price = coin['current_price']
                    price_change_24h = coin['price_change_percentage_24h']  # 24h change percentage

                    # Color formatting based on the values
                    # Name in orange, price in white, change in green/red
                    name_colored = f"{TerminalColors.ORANGE}{name}{TerminalColors.RESET}"
                    price_colored = f"{TerminalColors.WHITE}€{price}{TerminalColors.RESET}"

                    if price_change_24h >= 0:
                        change_colored = f"{TerminalColors.GREEN}+{price_change_24h:.2f}%{TerminalColors.RESET}"
                    else:
                        change_colored = f"{TerminalColors.RED}{price_change_24h:.2f}%{TerminalColors.RESET}"

                    # Print formatted and colored output
                    print(f"{name_colored}: {price_colored} ({change_colored})")

            except ValueError:
                print("Error: Failed to parse the response as JSON.")
        else:
            print(f"Failed to fetch data: {response.status_code}")

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        print(f"Error: A network error occurred - {e}")

# Call the function to fetch and display the prices
fetch_top_50_prices()
