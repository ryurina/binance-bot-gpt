import time
from binance.client import Client

# Replace YOUR_API_KEY and YOUR_API_SECRET with your own API keys
client = Client("YOUR_API_KEY", "YOUR_API_SECRET")

# Set the symbol and interval for the bot
symbol = "BTCUSDT"
interval = Client.KLINE_INTERVAL_1HOUR

# Set the number of periods to use for the moving average
periods = 3

while True:
    # Get the current ticker data
    ticker = client.fetch_ticker(symbol)
    price = ticker["lastPrice"]

    # Get the moving average
    klines = client.fetch_klines(symbol=symbol, interval=interval, limit=periods)
    close_prices = [float(kline[4]) for kline in klines]
    moving_average = sum(close_prices) / len(close_prices)

    # Calculate the percentage change
    change = (price - moving_average) / moving_average * 100

    # If the percentage change is above a threshold, buy or sell
    threshold = 0.5
    if change > threshold:
        # Buy
        print("Buying")
        client.order_market_buy(symbol=symbol, quantity=1)
    elif change < -threshold:
        # Sell
        print("Selling")
        client.order_market_sell(symbol=symbol, quantity=1)
    else:
        print("No action")

    # Wait for the next period
    time.sleep(interval)
