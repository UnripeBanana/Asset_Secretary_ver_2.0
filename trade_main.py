from config import NOTION_DOMESTIC_STOCK_TRADE_DB_ID
from notion.get_all_pages import get_all_pages

#-----------------------------------------
# 국내주식 거래내역 DB 업데이트
#-----------------------------------------
from domestic_stock_trade.read import 
from domestic_stock_trade.update import 
from trade.fifo import group_by_ticker, process_fifo

for page in get_all_pages(NOTION_DOMESTIC_STOCK_TRADE_DB_ID):
    # 각 페이지별로 데이터 읽기
    

    # 읽은 데이터 fifo처리


    # 데이터 업데이트






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
    
for page in get_all_pages(NOTION_DOMESTIC_STOCK_INFO_DB_ID):
    """
    # 임시로 노션 페이지 출력 확인
    print(page)
    print("\n\n")
    print(page["properties"])
    if page:
        break
    """
    
    # 티커 데이터 추출
    ticker = get_ticker(page)
    if not ticker:
        continue

    # 네이버증권에서 데이터 받아오기
    domestic_stock_info = get_domestic_stock_info(ticker) # dictionary

    # 노션 & CSV에 데이터 업로드
    update_domestic_stock_info_DB(page, domestic_stock_info)
