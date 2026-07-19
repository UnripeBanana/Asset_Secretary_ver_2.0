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
from charts.high_low import present_high_and_low
from charts.current_price import present_current_price

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

    # 최고가 최저가 표시
    present_high_and_low (ax, stock)

    # 현재가 표시
    present_current_price(ax, stock)
    
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
