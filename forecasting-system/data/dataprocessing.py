import numpy as np
# Makes the data stationary 
def compute_log_returns(price_series):

    log_prices = np.log(price_series)
    returns = log_prices.diff()

    returns = returns.dropna()

    return returns

def train_test_split(series, train_ratio):
    split_idx = int(len(series) * train_ratio)
    train = series.iloc[:split_idx]
    test = series.iloc[split_idx:]
    return train, test