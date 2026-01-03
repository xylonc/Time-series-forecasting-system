import numpy as np
import pandas as pd

# Makes the data stationary 
def compute_log_returns(price_series):

    log_prices = np.log(price_series)
    returns = log_prices.diff()

    returns = returns.dropna()

    return returns

def prepare_series(series: pd.Series) -> pd.Series:
    series = series.copy()
    
    series = series.replace([float("inf"), float("-inf")], float("nan"))
    series = series.dropna()
    
    series.index = pd.to_datetime(series.index)
    inferred_freq = pd.infer_freq(series.index)
    if inferred_freq is None:
        series = series.asfreq("B")
    else:
        series = series.asfreq(inferred_freq)

    return series

def train_test_split(series, train_ratio):
    split_idx = int(len(series) * train_ratio)
    train = series.iloc[:split_idx]
    test = series.iloc[split_idx:]
    return train, test

def reconstruct_price_series(
    last_price: float,
    log_return_preds: pd.Series
) -> pd.Series:
    
    cumulative_returns = log_return_preds.cumsum()
    price_preds = last_price * np.exp(cumulative_returns)
    return price_preds