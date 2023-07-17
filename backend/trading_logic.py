import alpaca_trade_api as tradeapi
# import talib
from config import API_KEY, SECRET_KEY

# Set up your Alpaca API credentials
BASE_URL = 'https://paper-api.alpaca.markets'  # Use the paper trading API URL for testing

# Connect to the Alpaca API
api = tradeapi.REST(API_KEY, SECRET_KEY, base_url=BASE_URL, api_version='v2')

def ema_crossover(symbol='AAPL', timeframe='1Min'):
    # Get historical data
    historical_data = api.get_barset(symbol, timeframe, limit=50).df[symbol]

    # Calculate the EMA(1) and EMA(7)
    ema_1 = ''#= talib.EMA(historical_data['close'], timeperiod=1)
    ema_7 = ''#= talib.EMA(historical_data['close'], timeperiod=7)

    # Check for crossover signals
    if ema_1[-2] < ema_7[-2] and ema_1[-1] > ema_7[-1]:
        # Place a buy options order
        option_symbol = 'AAPL20230721C150'  # Replace with the desired options symbol
        quantity = 1  # Replace with the desired quantity of options contracts
        order_type = 'market'  # Use 'market' for a market order, or choose another order type
        time_in_force = 'gtc'  # Use 'gtc' for "good 'til canceled", or choose another time in force

        try:
            api.submit_order(
                symbol=option_symbol,
                qty=quantity,
                side='buy',
                type=order_type,
                time_in_force=time_in_force
            )
            response = {'message': 'Buy order placed successfully!'}
        except Exception as e:
            response = {'error': f'Error placing buy order: {str(e)}'}

    else:
        response = {'message': 'No buy signal generated.'}

    return response

def get_market_data(api_key, api_secret, symbol):
    api = tradeapi.REST(api_key, api_secret, base_url=BASE_URL)
    market_data = api.get_barset(symbol, 'day', limit=100).df
    return market_data.to_json(orient='records')

print(get_market_data(API_KEY, SECRET_KEY, 'aapl'))