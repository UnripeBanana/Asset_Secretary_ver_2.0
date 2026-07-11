from config import NOTION_DOMESTIC_STOCK_INFO_DB_ID
from notion.get_all_pages import get_all_pages

#-----------------------------------------
# 국내주식 종목 DB 업데이트
#-----------------------------------------
from domestic_stock_info.read import get_ticker
from domestic_stock_info.data import get_domestic_stock_info
from domestic_stock_info.update import update_domestic_stock_info_DB

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

