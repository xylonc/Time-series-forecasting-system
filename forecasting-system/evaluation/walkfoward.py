import numpy as np

def walk_forward_validation(series, model_class, model_kwargs, initial_window):
    forecasts = []
    actuals = []

    for t in range(initial_window, len(series)):
        train = series[:t]
        test = series[t]

        model = model_class(**model_kwargs)
        model.fit(train)

        forecast = model.forecast(steps=1)[0]

        forecasts.append(forecast)
        actuals.append(test)

    return np.array(forecasts), np.array(actuals)
