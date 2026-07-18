import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# -----------------------------
# CSV 읽기
# -----------------------------
df = pd.read_csv("domestic_stock_info/csv/test_data.csv", dtype={"ticker": str})

ticker = "005930"

stock = df[df["ticker"] == ticker].copy()

stock["date"] = pd.to_datetime(stock["date"])
stock = stock.sort_values("date").reset_index(drop=True)

# -----------------------------
# 이동평균선 계산
# -----------------------------
stock["MA5"] = stock["close"].rolling(5).mean()
stock["MA20"] = stock["close"].rolling(20).mean()
stock["MA60"] = stock["close"].rolling(60).mean()
stock["MA120"] = stock["close"].rolling(120).mean()

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
# 이동평균선
# -----------------------------
ax.plot(x, stock["MA5"], color="orange", linewidth=1.2, label="5")
ax.plot(x, stock["MA20"], color="red", linewidth=1.2, label="20")
ax.plot(x, stock["MA60"], color="green", linewidth=1.2, label="60")
ax.plot(x, stock["MA120"], color="blue", linewidth=1.2, label="120")

ax.legend(loc="upper left")


# -----------------------------
# 최고가 / 최저가
# -----------------------------
high_idx = stock["high"].idxmax()
low_idx = stock["low"].idxmin()

high_price = stock.loc[high_idx, "high"]
low_price = stock.loc[low_idx, "low"]


# -----------------------------
# 축 설정
# -----------------------------

# 위/오른쪽 테두리 제거
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# y축을 오른쪽으로 이동
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")

# 오른쪽 spine만 표시
ax.spines["right"].set_visible(True)
"""
ax.tick_params(
    axis="y",
    left=False,
    labelleft=False,
    right=True,
    labelright=True
)
"""
ax.tick_params(
    axis="y",
    direction="out",
    length=3,
    colors="gray"
)

ax.spines["right"].set_color("#cccccc")

ax.set_xlim(-1, len(stock) + 4)

# 여백 조금 주기
price_min = stock["low"].min()
price_max = stock["high"].max()

margin = (price_max - price_min) * 0.05

"""
# y축을 0부터 보이게 설정
ax.set_ylim(
    bottom = price_min - margin,
    top = price_max + margin
)
"""

ax.set_ylim(
    price_min - margin,
    price_max + margin
)

# -----------------------------
# 최고가 표시
# -----------------------------
ax.plot(
    high_idx,
    high_price + 700,
    marker="v",                          # ▼ 표시
    color="gray",
    markersize=5
)

# 텍스트
ax.text(
    high_idx + 4,                      # 왼쪽으로 약간 이동
    high_price + 700,          # ▼와 같은 높이
    f"High Price {high_price:,}",
    va="center",
    ha="right",
    fontsize=8,
    color="gray"
)

# -----------------------------
# 최저가 표시
# -----------------------------
ax.plot(
    low_idx,
    low_price - 700,
    marker="^",                          # ▲ 표시
    color="gray",
    markersize=5
)

# 텍스트
ax.text(
    low_idx + 0.5,                       # 오른쪽으로 약간 이동
    low_price - 700,           # ▲와 같은 높이
    f"Low Price {low_price:,}",
    va="center",
    ha="left",
    fontsize=8,
    color="gray"
)

# -----------------------------
# 현재가 표시
# -----------------------------
last_close = stock.iloc[-1]["close"]
current_color = "#e53935" if last_close >= stock.iloc[-1]["open"] else "#1565c0"

# 현재가 수평선
ax.axhline(
    y=last_close,
    color="gray",
    linestyle="--",
    linewidth=1,
    alpha=0.6
)

# 현재가 라벨
ax.text(
    len(stock) + 0.5,      # 오른쪽 여백에 표시
    last_close,
    f"{last_close:,}",
    va="center",
    ha="left",
    fontsize=9,
    color="white",
    bbox=dict(
        boxstyle="round,pad=0.25",
        facecolor=current_color,
        edgecolor="none"
    )
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

date = "2026-07-14"
name = "삼성전자"
ticker = "005930"

title = f"charts/{date}_{name}_{ticker}.png"

plt.savefig(
    title,
    dpi=300,
    bbox_inches="tight"
)

plt.close()
