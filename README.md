# Binance Trading Bot

This is a simple trading bot that buys and sells based on the percentage change in price over a given period of time. It uses the binance-python library to access the Binance API and execute trades.

## Prerequisites

- Python 3
- binance-python library (https://github.com/binance-exchange/binance-python)
- Binance API keys (obtain them here: https://www.binance.com/en/api/manage)

## Usage

1. Clone this repository and navigate to the directory.

```
    git clone https://github.com/ryurina/binance-bot-gpt
    cd binance-bot-gpt
```

2. Replace the YOUR_API_KEY and YOUR_API_SECRET placeholders in the code with your own API keys.

3. Run the script.
```
    python trading_bot.py
```

4. The bot will start executing trades based on the percentage change in price over the past 3 intervals (which can be adjusted in the code).

## Configuration

You can configure the following parameters in the code:

- symbol: the symbol to trade (e.g. "BTCUSDT")
- interval: the interval to use for the moving average (e.g. Client.KLINE_INTERVAL_1HOUR)
- periods: the number of periods to use for the moving average
- threshold: the percentage change threshold for buying or selling

## Disclaimer

This is a sample trading bot for educational purposes only. It is not intended to be used for real trading. Use it at your own risk.

#### PS: This README.md and the code was written by ChatGPT (https://chat.openai.com)
