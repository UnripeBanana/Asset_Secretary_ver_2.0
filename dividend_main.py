from config import NOTION_DOMESTIC_STOCK_DIVIDEND_DB_ID
from notion.get_all_pages import get_all_pages

#-----------------------------------------
# 국내주식 거래내역 DB 업데이트
#-----------------------------------------
from domestic_stock_trade.read import read_domestic_stock_trade
from domestic_stock_trade.update import update_domestic_stock_trade_DB

for page in get_all_pages(NOTION_DOMESTIC_STOCK_TRADE_DB_ID):
    # 각 페이지별로 데이터 읽기
    properties = read_domestic_stock_dividend(page)
    
    # 노션에 데이터 업데이트
    update_domestic_stock_trade_DB(properties)
