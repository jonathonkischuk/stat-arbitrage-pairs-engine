from engine.fetch import fetch_pair_data
from engine.pairs import test_cointegration, zscore
from engine.engine import generate_trade_signals
from engine.performance import calculate_returns, compute_cumulative
from visualize.plotter import add_chart_data, show_chart_viewer


pairs = [
    ("KO", "PEP"), ("V", "MA"), ("F", "GM"), ("BA", "EADSY"),
    ("XOM", "CVX"), ("JPM", "BAC"), ("LMT", "NOC"), ("RTX", "GD"), ("HII", "GD")
]

for stock1, stock2 in pairs:
    print(f"Processing Pair: {stock1} / {stock2}")
    df = fetch_pair_data(stock1, stock2)

    hedge_ratio, spread, pval = test_cointegration(df[stock1], df[stock2])
    print(f"ADF p-value: {pval:.4f}, Hedge Ratio: {hedge_ratio:.4f}")

    if pval < 0.05:
        positions = generate_trade_signals(spread)
        returns = calculate_returns(df, hedge_ratio, positions)
        cumulative = compute_cumulative(returns)

        add_chart_data(f"{stock1}_{stock2}", cumulative, zscore(spread))


show_chart_viewer()

