import yfinance as yf
import json
from datetime import datetime


def get_stock_prices(ticker, days):
    try:
      
        stock_data = yf.download(ticker, period=f"{days}d", interval="1d")
        stock_data.index = stock_data.index.strftime("%d/%m/%Y")
        stock_json = stock_data.to_json(orient="index")
        stock_prices = json.loads(stock_json)

        return stock_prices

    except Exception as e:
        return {"error": str(e)}

ticker = "AAPL" 
days = 30  
prices = get_stock_prices(ticker, days)
print(prices)