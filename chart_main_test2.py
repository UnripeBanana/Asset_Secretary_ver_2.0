import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# -----------------------------
# CSV 읽기
# -----------------------------
df = pd.read_csv("domestic_stock_info/csv/price_history.csv")

ticker = "005930"

stock = df[df["ticker"] == ticker].copy()

stock["date"] = pd.to_datetime(stock["date"])
stock = stock.sort_values("date").reset_index(drop=True)

# -----------------------------
# Figure 생성
# -----------------------------
fig, ax = plt.subplots(figsize=(15, 8))

x = np.arange(len(stock))

candle_width = 0.7

# -----------------------------
# 캔들 그리기
# -----------------------------
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

# -----------------------------
# 축 설정
# -----------------------------
ax.set_xlim(-1, len(stock))

# 여백 조금 주기
price_min = stock["low"].min()
price_max = stock["high"].max()

margin = (price_max - price_min) * 0.05

ax.set_ylim(
    price_min - margin,
    price_max + margin
)

# -----------------------------
# 날짜 표시 (매주 첫 거래일)
# -----------------------------
tick_positions = []
tick_labels = []

last_week = None

for i, row in stock.iterrows():

    week = row["date"].isocalendar().week

    if week != last_week:
        tick_positions.append(i)
        tick_labels.append(row["date"].strftime("%m-%d"))
        last_week = week

ax.set_xticks(tick_positions)
ax.set_xticklabels(
    tick_labels,
    rotation=0,
    fontsize=9
)

# -----------------------------
# 스타일
# -----------------------------
ax.grid(
    linestyle="--",
    alpha=0.3
)

ax.set_facecolor("white")
fig.patch.set_facecolor("white")

# 위/오른쪽 테두리 제거
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# -----------------------------
# 저장
# -----------------------------
plt.tight_layout()

plt.savefig(
    "charts/005930.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()
