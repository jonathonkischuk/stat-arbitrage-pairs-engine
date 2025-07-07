import yfinance as yf
import pandas as pd
from pathlib import Path


def fetch_pair_data(ticker1, ticker2, start="2015-01-01", end="2024-12-31"):
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    df1 = yf.download(ticker1, start=start, end=end, group_by="ticker", auto_adjust=True)
    df2 = yf.download(ticker2, start=start, end=end, group_by="ticker", auto_adjust=True)

    # Handle single or multi-index column structure
    if isinstance(df1.columns, pd.MultiIndex):
        df1 = df1.xs("Close", axis=1, level=1).rename(columns={ticker1: ticker1})
    else:
        df1 = df1["Close"].rename(ticker1)

    if isinstance(df2.columns, pd.MultiIndex):
        df2 = df2.xs("Close", axis=1, level=1).rename(columns={ticker2: ticker2})
    else:
        df2 = df2["Close"].rename(ticker2)

    df = pd.concat([df1, df2], axis=1).dropna()
    df.to_csv(data_dir / f"{ticker1}_{ticker2}.csv")
    return df
