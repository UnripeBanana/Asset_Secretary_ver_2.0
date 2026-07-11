from config import NOTION_DOMESTIC_STOCK_TRADE_DB_ID
from notion.get_all_pages import get_all_pages
from notion.client import notion
from collections import defaultdict

#-----------------------------------------
# 국내주식 거래내역 DB 업데이트
#-----------------------------------------
from domestic_stock_trade.read import read_domestic_stock_trade
from trade.fifo import process_fifo
from domestic_stock_trade.update import update_domestic_stock_trade_DB

# 각 페이지별로 데이터 읽기
groups = defaultdict(list)

for page in get_all_pages(NOTION_DOMESTIC_STOCK_TRADE_DB_ID):
    trade = read_domestic_stock_trade(page)  # trade : {'page_id': '9446e5ae-e083-82af-83c7-81578d26b1bf', 'ticker': '삼성전자', 'type': '매수', 'date': '2026-06-19', 'qty': 1, 'price': 349000, 'amount': 349000}
    groups[trade["ticker"]].append(trade)    # groups : defaultdict(<class 'list'>, {'삼성전자': [{'page_id': '9446e5ae-e083-82af-83c7-81578d26b1bf', 'ticker': '삼성전자', 'type': '매수', 'date': '2026-06-19', 'qty': 1, 'price': 349000, 'amount': 349000}]})

# 읽은 데이터 fifo처리
for trades in groups.values():
    trades.sort(key=lambda x: x["date"])

results = process_fifo(groups)

# 노션에 데이터 업데이트
update_domestic_stock_trade_DB(results)



