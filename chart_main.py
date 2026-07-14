import pandas as pd
import mplfinance as mpf

df = pd.read_csv("domestic_stock_info/csv/price_history.csv")

# print(df.head())

ticker = "005930"

stock = df[df["ticker"] == ticker].copy()

stock["date"] = pd.to_datetime(stock["date"])

stock = stock.set_index("date")

print(stock.head())

mc = mpf.make_marketcolors(
    up='#e53935',      # 상승(빨강)
    down='#1565c0',    # 하락(파랑)
    edge='inherit',
    wick='inherit',
    volume='inherit'
)

style = mpf.make_mpf_style(
    marketcolors=mc,
    gridstyle='--',
    facecolor='white',
    figcolor='white'
)

mpf.plot(stock, type="candle")

mpf.plot(
    stock,
    type="candle",
    style = style,
    savefig="charts/005930.png"
)
