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
from notion.client import notion

# 나중에는
# make_chart 함수 하나, delete_chart 하나 update_chart 하나 이렇게 구성하는 것도 괜찮을 듯. 깔끔하게

DOMESTIC_STOCK_CSV_PATH = Path("domestic_stock_info/csv/test_data.csv")
# 실제 데이터 경로 : Path("domestic_stock_info/csv/price_history.csv") 
# 테스트용 경로 : Path("domestic_stock_info/csv/test_data.csv")

for page in get_all_pages(NOTION_DOMESTIC_STOCK_INFO_DB_ID):
    # 티커 데이터 추출
    ticker = get_ticker(page)
    if not ticker:
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

    # 노션에 있는 기존 이미지 삭제
    found = False
    heading_block_id = None

    blocks = notion.blocks.children.list(block_id=page["id"])
        
    for block in blocks["results"]:
    
        # "3개월 차트" 제목을 찾음
        if (
            block["type"] == "heading_2"
            and block["heading_2"]["rich_text"][0]["plain_text"] == "3개월 차트"
        ):
            found = True
            heading_block_id = block["id"]
            continue
    
        # 제목 바로 다음 image 삭제
        if found and block["type"] == "image":
            notion.blocks.delete(block["id"])
            break
    
    # 노션 업로드
    chart_url = (
        "https://raw.githubusercontent.com/"
        "UnripeBanana/Asset_Secretary_ver_2.0/main/"
        f"charts/image/{name}_{ticker}.png"
    )

    notion.blocks.children.append(
        block_id=page["id"],
        after=heading_block_id,
        children=[
            {
                "object": "block",
                "type": "image",
                "image": {
                    "type": "external",
                    "external": {
                        "url": chart_url
                    }
                }
            }
        ]
    )
