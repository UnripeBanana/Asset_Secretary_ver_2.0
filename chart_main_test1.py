import pandas as pd
import mplfinance as mpf
import matplotlib.dates as mdates

df = pd.read_csv("domestic_stock_info/csv/price_history.csv")

ticker = "005930"

stock = df[df["ticker"] == ticker].copy()

stock["date"] = pd.to_datetime(stock["date"])

stock = stock.set_index("date")

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

fig, axlist = mpf.plot(
    stock,
    type="candle",
    volume=True,
    style=style,
    update_width_config=dict(
        candle_linewidth=0
    ),
    returnfig=True,
)

price_ax = axlist[0]

# Y축
price_ax.set_ylim(bottom=0)

# X축
price_ax.xaxis.set_major_locator(
    mdates.WeekdayLocator(byweekday=mdates.MO)
)
price_ax.xaxis.set_major_formatter(
    mdates.DateFormatter('%m-%d')
)

# 저장
fig.savefig(
    "charts/005930.png",
    dpi=200,
    bbox_inches="tight"
)
