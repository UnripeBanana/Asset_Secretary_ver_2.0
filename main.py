from config import NOTION_DOMESTIC_STOCK_INFO_DB_ID
from notion.get_all_pages import get_all_pages

#-----------------------------------------
# 국내주식 종목 DB 업데이트
#-----------------------------------------
from domestic_stock.read import get_ticker
from domestic_stock.data import get_domestic_stock_info

for page in get_all_pages(NOTION_DOMESTIC_STOCK_INFO_DB_ID):
    # 티커 데이터 추출
    ticker = get_ticker(page)
    if not ticker:
        continue

    # 네이버증권에서 데이터 받아오기
    domestic_stock_info = get_domestic_stock_info(ticker)

    # 노션에 데이터 업로드
    update_stock_DB(page, stock_info)

    # CSV에 데이터 업로드


"""
pages = get_all_pages(NOTION_DOMESTIC_STOCK_INFO_DB_ID)

for page in pages:
    print(page)
    if page:
        break
##########################
domestic_stock_main(get_all_pages(NOTION_DOMESTIC_STOCK_INFO_DB_ID))

    for page in pages:
        ticker = get_ticker(page)

def get_ticker(page):
    ticker_data = page["properties"]["티커"]["rich_text"]

    if not ticker_data:
        return None

    return ticker_data[0]["plain_text"]
"""
