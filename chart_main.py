from config import NOTION_DOMESTIC_STOCK_INFO_DB_ID
from notion.get_all_pages import get_all_pages
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# -----------------------------
# 국내주식 차트 생성
# -----------------------------
from domestic_stock_info.read import get_ticker
from charts.read_csv import read_csv
from charts.candle_chart import make_candle_chart
from charts.meanline import meanline
from charts.axis import set_axis

DOMESTIC_STOCK_CSV_PATH = Path("domestic_stock_info/csv/test_data.csv")
# 실제 데이터 경로 : Path("domestic_stock_info/csv/price_history.csv") 
# 테스트용 경로 : Path("domestic_stock_info/csv/test_data.csv")

for page in get_all_pages(NOTION_DOMESTIC_STOCK_INFO_DB_ID):
    # 티커 데이터 추출
    ticker = get_ticker(page)
    if not ticker:
        continue

    # 임시로 삼성 테스트 데이터만 사용
    if ticker != "005930":
        continue

    # CSV 파일 읽어오기
    stock = read_csv(DOMESTIC_STOCK_CSV_PATH, ticker)

    # chart 사이즈 설정
    fig, ax = plt.subplots(figsize=(15, 8))
    x = np.arange(len(stock))

    # 캔들차트 생성
    make_candle_chart(ax, stock)

    # 이동평균선
    meanline(ax, stock, x)

    # 축 설정
    set_axis(ax, stock)

    
    # 저장
    plt.tight_layout()
    name = page["properties"]["종목"]["title"][0]["plain_text"]
    
    title = f"charts/image/{name}_{ticker}.png"
    
    plt.savefig(
        title,
        dpi=300,
        bbox_inches="tight"
    )




"""

# -----------------------------
# 최고가 / 최저가
# -----------------------------
high_idx = stock["high"].idxmax()
low_idx = stock["low"].idxmin()

high_price = stock.loc[high_idx, "high"]
low_price = stock.loc[low_idx, "low"]




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
# 현재가 표시 (네이버증권 스타일)
# -----------------------------
last_close = stock.iloc[-1]["close"]

# 당일 상승/하락에 따라 색상 결정
current_color = (
    "#e53935"
    if last_close >= stock.iloc[-1]["open"]
    else "#1565c0"
)

ax.annotate(
    f"{last_close:,}",
    xy=(len(stock), last_close),             # 화살표 끝
    xytext=(len(stock) + 4.2, last_close),   # 박스 위치
    ha="left",
    va="center",
    fontsize=12,
    fontweight="bold",
    color="white",

    bbox=dict(
        boxstyle="larrow,pad=0.35",
        fc=current_color,
        ec=current_color
    ),

    annotation_clip=False
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



plt.close()
"""
