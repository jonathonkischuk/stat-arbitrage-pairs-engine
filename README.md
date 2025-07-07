# 📈 Stat-Arbitrage Pairs Trading Engine

A modular statistical arbitrage engine to detect, simulate, and analyze mean-reverting relationships between pairs of stocks using cointegration, rolling hedge ratios, and z-score thresholds.

---

## 🔍 Strategy Logic

This engine identifies **cointegrated asset pairs** using the **Augmented Dickey-Fuller (ADF) test**, computes a **dynamic hedge ratio** with **rolling OLS**, and tracks spread deviations with a **rolling Z-Score**.

### ✅ Sample Pairs:
- KO/PEP (Coca-Cola vs PepsiCo)
- V/MA (Visa vs Mastercard)
- JPM/BAC (JP Morgan vs Bank of America)
- XOM/CVX (ExxonMobil vs Chevron)
- LMT/NOC, RTX/GD, BA/EADSY, F/GM, HII/GD

---

## 🧠 Features

- 🧮 Cointegration detection via ADF test
- 🧾 Rolling hedge ratio with OLS regression
- 📊 Dynamic z-score calculation
- 💸 Slippage and commission modeling
- 📈 Equity curve + trade signal visualization
- 🐳 Docker-ready deployment

---

## 📁 Project Structure

```bash
stat-arb-pairs-engine/
├── data/ # Historical pair data
├── engine/ # Trading logic + math
├── visualize/ # Charts
├── reports/ # Output PNGs/CSVs
├── main.py # Pipeline entry point
├── requirements.txt # Python dependencies
└── Dockerfile # Containerization
```
---

## 🐍 Run Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
---

## 🐳 Run in Docker (No Chart Display)

```bash
Copy
Edit
docker build -t stat-arb-pairs-engine .
docker run --rm -v $(pwd)/reports:/app/reports stat-arb-pairs-engine
```
---

## 📊 Sample Output

ADF p-value: 0.018 — cointegrated

Equity Curve: reports/KO_PEP_equity_curve.png

Cumulative Return: ~22% over 3 years
