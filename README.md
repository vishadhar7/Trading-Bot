# Trading Bot – Binance Futures Testnet

## Setup

1. Clone repo
2. Install dependencies:
   pip install python-binance
   pip install python-dotenv

3. Add .env file with API keys

## Usage

### Market Order
Run in terminal
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
Run in terminal
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Features

- Market & Limit Orders
- Input validation
- Logging to bot.log
- Error handling

## Assumptions

- Using Binance Futures Testnet
- Quantity is valid per Binance rules