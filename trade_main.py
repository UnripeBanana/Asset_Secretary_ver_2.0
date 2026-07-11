from config import NOTION_DOMESTIC_STOCK_TRADE_DB_ID
from notion.get_all_pages import get_all_pages
from collections import defaultdict

#-----------------------------------------
# 국내주식 거래내역 DB 업데이트
#-----------------------------------------
from domestic_stock_trade.read import read_domestic_stock_trade
from trade.fifo import process_fifo
from domestic_stock_trade.update import update_domestic_stock_trade_DB

# 각 페이지별로 데이터 읽기
groups = defaultdict(list)
trades = []

for page in get_all_pages(NOTION_DOMESTIC_STOCK_TRADE_DB_ID):
    trade = read_domestic_stock_trade(page)  
    trades.append(trade)  
    groups[trade["ticker"]].append(trade)   
    
# 읽은 데이터 fifo처리
for trades in groups.values():
    trades.sort(key=lambda x: x["date"])

results = process_fifo(groups)

# 노션에 데이터 업데이트
update_domestic_stock_trade_DB(results, trades)



