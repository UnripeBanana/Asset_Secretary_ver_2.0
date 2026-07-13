from config import NOTION_DOMESTIC_STOCK_INFO_DB_ID, NOTION_KRX_GOLD_INFO_DB_ID, NOTION_DOMESTIC_BOND_ETF_INFO_DB_ID
from notion.get_all_pages import get_all_pages

#-----------------------------------------
# 국내주식 종목 DB 업데이트
#-----------------------------------------
from domestic_stock_info.read import get_ticker
from domestic_stock_info.data import get_domestic_stock_info
from domestic_stock_info.update import update_domestic_stock_info_DB

for page in get_all_pages(NOTION_DOMESTIC_STOCK_INFO_DB_ID):
    # 티커 데이터 추출
    ticker = get_ticker(page)
    if not ticker:
        continue

    # 네이버증권에서 데이터 받아오기
    domestic_stock_info = get_domestic_stock_info(ticker) # dictionary

    # 노션에 데이터 업로드
    update_domestic_stock_info_DB(page, domestic_stock_info)


#-----------------------------------------
# KRX 금현물 종목 DB 업데이트
#-----------------------------------------
from krx_gold_info.data import get_krx_gold_info
from krx_gold_info.update import update_krx_gold_info_DB

for page in get_all_pages(NOTION_KRX_GOLD_INFO_DB_ID):
    # 네이버증권에서 데이터 받아오기
    krx_gold_info = get_krx_gold_info()

    # 노션에 데이터 업로드
    update_krx_gold_info_DB(page, krx_gold_info)


#-----------------------------------------
# 국내 채권 ETF 종목 DB 업데이트
#-----------------------------------------
from domestic_stock_info.read import get_ticker
from domestic_stock_info.data import get_domestic_stock_info
from domestic_stock_info.update import update_domestic_stock_info_DB

for page in get_all_pages(NOTION_DOMESTIC_BOND_ETF_INFO_DB_ID):
    # 티커 데이터 추출
    ticker = get_ticker(page)
    if not ticker:
        continue

    # 네이버증권에서 데이터 받아오기
    domestic_stock_info = get_domestic_stock_info(ticker) # dictionary

    # 노션에 데이터 업로드
    update_domestic_stock_info_DB(page, domestic_stock_info)
