import numpy as np


def zscore(series):
    return (series - series.mean()) / series.std()



def generate_trade_signals(spread, entry_threshold=2, exit_threshold=0):
    z = zscore(spread)
    positions = []

    for i in range(len(z)):
        if z[i] > entry_threshold:
            positions.append(-1)    # Short Spread: Short Stock1, Long Stock2
        elif z[i] < -entry_threshold:
            positions.append(1)     # Long Spread: Long Stock1, Short Stock2
        elif abs(z[i]) < exit_threshold:
            positions.append(0)     # Exit
        else:
            positions.append(positions[-1] if i > 0 else 0)
    return positions