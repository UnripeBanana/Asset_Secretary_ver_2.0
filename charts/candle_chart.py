import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def make_candle_chart(stock):
for i, row in stock.iterrows():
    open_price = row["open"]
    high_price = row["high"]
    low_price = row["low"]
    close_price = row["close"]

    # 상승 / 하락 색상
    color = "#e53935" if close_price >= open_price else "#1565c0"

    # 심지
    ax.vlines(
        x=i,
        ymin=low_price,
        ymax=high_price,
        color=color,
        linewidth=1.2
    )

    # 몸통
    body_bottom = min(open_price, close_price)
    body_height = abs(close_price - open_price)

    # 시가 = 종가인 경우도 보이도록
    if body_height == 0:
        body_height = 1

    rect = Rectangle(
        (i - candle_width / 2, body_bottom),
        candle_width,
        body_height,
        facecolor=color,
        edgecolor="none"     # ← 테두리 완전 제거
    )

    ax.add_patch(rect)

