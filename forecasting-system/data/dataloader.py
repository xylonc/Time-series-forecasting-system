import yfinance as yf
import pandas as pd
import numpy as np

def load_price_data(ticker, start_date, end_date):
    data = yf.download(
        ticker,
        start = start_date,
        end = end_date,
        progress=False
    )
    if data.empty:
        raise ValueError(f"There seems to be an error with the ticker '{ticker}'")
    
    prices = data["Adj Close"]
    prices.name = ticker
    
    return prices  
    

    
