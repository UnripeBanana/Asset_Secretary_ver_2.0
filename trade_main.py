from config import NOTION_DOMESTIC_STOCK_TRADE_DB_ID, NOTION_KRX_GOLD_TRADE_DB_ID
from notion.get_all_pages import get_all_pages
from collections import defaultdict
from trade.fifo import process_fifo

"""
#-----------------------------------------
# 국내주식 거래내역 DB 업데이트
#-----------------------------------------
from domestic_stock_trade.read import read_domestic_stock_trade
from domestic_stock_trade.update import update_domestic_stock_trade_DB

# 각 페이지별로 데이터 읽기
domestic_stock_groups = defaultdict(list)

for page in get_all_pages(NOTION_DOMESTIC_STOCK_TRADE_DB_ID):
    domestic_stock_trade = read_domestic_stock_trade(page)  
    domestic_stock_groups[domestic_stock_trade["ticker"]].append(domestic_stock_trade)   
    
# 읽은 데이터 fifo처리
for trades in domestic_stock_groups.values():
    trades.sort(key=lambda x: x["date"])

domestic_stock_results = process_fifo(domestic_stock_groups)

# 노션에 데이터 업데이트
update_domestic_stock_trade_DB(domestic_stock_results)
"""

#-----------------------------------------
# KRX 금현물 거래내역 DB 업데이트
#-----------------------------------------
from krx_gold_trade.read import read_krx_gold_trade
from krx_gold_trade.update import update_krx_gold_trade_DB

# 각 페이지별로 데이터 읽기
krx_gold_groups = defaultdict(list)

for page in get_all_pages(NOTION_KRX_GOLD_TRADE_DB_ID):
    krx_gold_trade = read_krx_gold_trade(page)  
    krx_gold_groups[krx_gold_trade["ticker"]].append(krx_gold_trade)   
    
# 읽은 데이터 fifo처리
for trades in krx_gold_groups.values():
    trades.sort(key=lambda x: x["date"])

krx_gold_results = process_fifo(krx_gold_groups)

# 노션에 데이터 업데이트
update_krx_gold_trade_DB(krx_gold_results)
