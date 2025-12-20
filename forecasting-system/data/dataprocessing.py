import numpy as np
# Makes the data stationary 
def prepare_series(price_series):

    log_prices = np.log(price_series)
    returns = log_prices.diff()

    returns = returns.dropna()

    return returns
