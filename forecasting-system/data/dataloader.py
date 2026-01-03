import yfinance as yf
import pandas as pd
from Exceptions.PriceColumnNotFoundException import PriceColumnNotFoundException


def load_price_data(ticker, start, end) -> pd.Series:
    data = yf.download(ticker, start=start, end=end, progress=False , auto_adjust= True)

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    if "Adj Close" in data.columns:
        return data["Adj Close"]
    elif "Close" in data.columns:
        print("Warning: Using Close instead of Adjusted Close")
        return data["Close"]
    else:
        raise PriceColumnNotFoundException(
            f"No price column found. Columns: {list(data.columns)}"
        )
