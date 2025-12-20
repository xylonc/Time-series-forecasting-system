class NaiveModel:
    def fit(self, series):
        self.mean = series.mean()

    def forecast(self, steps):
        return [self.mean] * steps
