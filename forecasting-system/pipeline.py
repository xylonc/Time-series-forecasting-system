from config import *
from data.dataloader import load_price_data, compute_log_returns , prepare_series
from evaluation.diagnostics import adf_test
from evaluation.metric import rmse , directional_accuracy
from models.arimamodel import ARIMAModel

def train_test_split(series, train_ratio):
    split_idx = int(len(series) * train_ratio)
    train = series.iloc[:split_idx]
    test = series.iloc[split_idx:]
    return train, test

def run_pipeline():
    prices = load_price_data(TICKER, START, END)
    series = prepare_series(prices, method="log_return")

    adf = adf_test(series)
    print("Stationary:", adf["is_stationary"])

    train, test = train_test_split(series, TRAIN_RATIO)

    model = ARIMAModel(order=(1,0,1))
    model.fit(train)

    preds = model.forecast(len(test))

    print("RMSE:", rmse(test, preds))
    print("DA:", directional_accuracy(test, preds))
