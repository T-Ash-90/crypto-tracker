import requests

def fetch_prices():
    coin_ids = "bitcoin,ethereum,litecoin,ripple,dash,monero,digibyte,dogecoin,solana,bitcoin-cash"
    vs_currency = "eur"
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_ids}&vs_currencies={vs_currency}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        try:
            prices = response.json()
        except ValueError:
            print("Error: Failed to parse JSON response.")
            return

        if not prices:
            print("Error: No price data found.")
            return

        sorted_coin_ids = sorted(coin_ids.split(","))

        for coin_id in sorted_coin_ids:
            coin_data = prices.get(coin_id)
            if coin_data and vs_currency in coin_data:
                print(f"{coin_id.upper()}: €{coin_data[vs_currency]}")
            else:
                print(f"{coin_id.upper()}: Price data not available.")

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: Network problem (e.g., DNS failure, refused connection).")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")

if __name__ == "__main__":
    fetch_prices()
