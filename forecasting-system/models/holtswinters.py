from statsmodels.tsa.holtwinters import ExponentialSmoothing

class HoltWintersModel:
    def fit(self, series):
        self.model = ExponentialSmoothing(
            series,
            trend="add",
            seasonal=None
        ).fit()

    def forecast(self, steps):
        return self.model.forecast(steps)
