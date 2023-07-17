from flask import Flask, jsonify, request
from backend.trading_logic import ema_crossover
from trading_logic import get_market_data

app = Flask(__name__)

@app.route('/api/ema-crossover', methods=['GET'])
def ema_crossover_route():
    symbol = request.args.get('symbol', 'AAPL')  # Default symbol is AAPL
    timeframe = request.args.get('timeframe', '1Min')  # Default timeframe is 1 minute

    response = ema_crossover(symbol, timeframe)

    return jsonify(response)

@app.route('/api/marketdata')
def fetch_market_data():
    api_key = '<YOUR_API_KEY>'
    api_secret = '<YOUR_API_SECRET>'
    symbol = '<SYMBOL>'
    
    market_data = get_market_data(api_key, api_secret, symbol)
    return jsonify(market_data)

if __name__ == '__main__':
    app.run(debug=True)