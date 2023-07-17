# Importing the API and instantiating the REST client according to our keys
from alpaca.trading.client import TradingClient
from config import API_KEY, SECRET_KEY
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

# Getting account information and printing it
def print_acc_info()  -> None:
    account = trading_client.get_account()
    for property_name, value in account:
        print(f"\"{property_name}\": {value}")

# print_acc_info()

def buy_market_order(symbol="BTC/USD", qty=1, side=OrderSide.BUY, tif=TimeInForce.GTC) -> None:
    # Setting parameters for our buy order
    market_order_data = MarketOrderRequest(
                        symbol=symbol,
                        qty=qty,
                        side=side,
                        time_in_force=tif
                    )
    market_order = trading_client.submit_order(market_order_data)
    for property_name, value in market_order:
        print(f"\"{property_name}\": {value}")

# buy_market_order()

def get_all_positions() -> None:
    positions = trading_client.get_all_positions()
    for position in positions:
        for property_name, value in position:
            print(f"\"{property_name}\": {value}")

# get_all_positions()