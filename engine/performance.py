def calculate_returns(df, hedge_ratio, positions):
    stock1_ret = df.iloc[:, 0].pct_change()
    stock2_ret = df.iloc[:, 1].pct_change()
    spread_ret = stock1_ret - hedge_ratio * stock2_ret
    strategy_ret = spread_ret * positions

    return strategy_ret.fillna(0)


def compute_cumulative(strategy_ret):
    return (1 + strategy_ret).cumprod()
