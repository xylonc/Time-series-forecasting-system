import yfinance as yf
import pandas as pd
import numpy as np
from Exceptions.Exceptions import PriceColumnNotFound

def load_price_data(ticker, start_date, end_date):
    data = yf.download(
        ticker,
        start = start_date,
        end = end_date,
        progress=False
    )
    if data.empty:
        raise ValueError(f"There seems to be an error with the ticker '{ticker}'")
    
    if "Adj Close" in data.columns:
        prices = data["Adj Close"]
    elif "Close" in data.columns:
        prices = data["Close"]
        print("Warning: Using Close instead of Adjusted Close as Adjusted close does not exist,likely due to oudated yfinance")
    else:
        raise PriceColumnNotFound(
            "Price column not found."
            f"Only have: {list(data.columns)}"
        )
    prices.name = ticker
    return prices  
    

    
