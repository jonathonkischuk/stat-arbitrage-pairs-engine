import numpy as np
from scipy import stats
import pandas as pd

def test_cointegration(series1, series2):
    # Ensure alignment
    series1, series2 = series1.align(series2, join="inner")

    # Convert to numpy arrays
    y = series1.values
    x = series2.values

    # Add constant manually for intercept
    X = np.vstack([np.ones(len(x)), x]).T
    beta = np.linalg.lstsq(X, y, rcond=None)[0][1]  # beta (hedge ratio)

    spread = y - beta * x

    # ADF alternative: mean-reversion score = autocorrelation lag-1 (quick and dirty)
    autocorr = np.corrcoef(spread[:-1], spread[1:])[0, 1]
    mean_reverting_score = 1 - autocorr  # Closer to 1 means more mean-reverting

    return beta, pd.Series(spread, index=series1.index), mean_reverting_score

def zscore(series):
    return (series - series.mean()) / series.std()

