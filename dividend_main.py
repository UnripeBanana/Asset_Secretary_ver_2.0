from config import NOTION_DOMESTIC_STOCK_DIVIDEND_DB_ID
from notion.get_all_pages import get_all_pages

#-----------------------------------------
# 국내주식 거래내역 DB 업데이트
#-----------------------------------------
from dividend.read import read_dividend
from net_profit import net_profit

for page in get_all_pages(NOTION_DOMESTIC_STOCK_TRADE_DB_ID):
    # 각 페이지별로 데이터 읽기
    profit = read_dividend(page)
    
    # 노션에 데이터 업데이트
    net_profit("dividend", profit)
