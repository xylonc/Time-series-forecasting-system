from config import *
from data.dataloader import load_price_data 
from data.dataprocessing import compute_log_returns  , train_test_split , prepare_series , reconstruct_price_series
from evaluation.diagnostics import adf_test
from evaluation.metric import rmse , directional_accuracy
from models.arimamodel import ARIMAModel
from Plots.plotting import plot_forecast

def run_pipeline(ticker):
    print(f"Running pipeline for {ticker}")
    
    prices = load_price_data(ticker, START, END)
    returns = compute_log_returns(prices) #returns not prices
    series = prepare_series(returns)
   
    adf = adf_test(series)
    print("Stationary:", adf["is_stationary"])

    train, test = train_test_split(series, TRAIN_RATIO)

    model = ARIMAModel(order=(1,0,1)) #next todo figure out using ACF better values
    model.fit(train)
    

    preds = model.forecast(len(test), index=test.index)
    
    print("RMSE:", rmse(test, preds))
    #print("DA:", directional_accuracy(test, preds))
    
    train_len = len(train)
    train_prices = prices.iloc[:train_len]
    test_prices = prices.iloc[train_len: train_len + len(test)]
    last_price = prices.iloc[len(train)]

    price_preds = reconstruct_price_series(last_price, preds)
    
    plot_forecast(
        train=train_prices,
        test=test_prices,
        preds=price_preds,
        ticker=ticker
    )
    
    return preds
