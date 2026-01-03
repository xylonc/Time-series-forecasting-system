import matplotlib.pyplot as plt

def plot_forecast(train, test, preds, ticker):
    plt.figure(figsize=(12, 6))

    plt.plot(train.index, train, label="Train")
    plt.plot(test.index, test, label="Test", color="black")
    plt.plot(preds.index, preds, label="Forecast", linestyle="--")

    plt.title(f"ARIMA Forecast for {ticker}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)

    plt.show()
