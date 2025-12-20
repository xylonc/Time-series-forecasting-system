from statsmodels.tsa.arima.model import ARIMA

class ARIMAModel:
    def __init__(self, order):
        self.order = order
        self.model = None

    def fit(self, series):
        self.model = ARIMA(series, order=self.order).fit()

    def forecast(self, steps):
        return self.model.forecast(steps=steps)
