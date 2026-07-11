from config import NOTION_DOMESTIC_STOCK_TRADE_DB_ID
from notion.get_all_pages import get_all_pages

#-----------------------------------------
# 국내주식 거래내역 DB 업데이트
#-----------------------------------------
from domestic_stock_trade.read import 
from domestic_stock_trade.update import 
from trade.fifo import group_by_ticker, process_fifo

for page in get_all_pages(NOTION_DOMESTIC_STOCK_TRADE_DB_ID):
    






def domestic_stock_trade_main(NOTION_TRADE_DB_ID):
    trades = read_trade_db(NOTION_TRADE_DB_ID)
    trades.sort(key=lambda x: x["date"])
    
    groups = group_by_ticker(trades)
    results = process_fifo(groups)
    
    for ticker, result in results.items():
        # 잔량 업데이트
        for page_id, qty in result["remaining"].items():
            update_trade_page(
                page_id=page_id,
                remaining=qty
            )
    
        # 실현수익 업데이트
        for page_id, profit in result["profit_by_sell"].items():
            update_trade_page(
                page_id=page_id,
                profit=profit
            )
    
