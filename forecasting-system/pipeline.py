from config import *
from data.dataloader import load_price_data 
from data.dataprocessing import compute_log_returns  , train_test_split
from evaluation.diagnostics import adf_test
from evaluation.metric import rmse , directional_accuracy
from models.arimamodel import ARIMAModel

def run_pipeline():
    prices = load_price_data(TICKER, START, END)
    series = compute_log_returns(prices)

    adf = adf_test(series)
    print("Stationary:", adf["is_stationary"])

    train, test = train_test_split(series, TRAIN_RATIO)

    model = ARIMAModel(order=(1,0,1))
    model.fit(train)

    preds = model.forecast(len(test))

    print("RMSE:", rmse(test, preds))
    #print("DA:", directional_accuracy(test, preds))
