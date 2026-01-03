from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

class ARIMAModel:
    def __init__(self, order):
        self.order = order
        self.model = None

    def fit(self, series):
        self.model = ARIMA(series, order=self.order).fit()

    def forecast(self, steps , index=None):
        preds = self.model.forecast(steps=steps)
        
        if index is not None:
            preds = pd.Series(preds, index=index)
            
        return preds
