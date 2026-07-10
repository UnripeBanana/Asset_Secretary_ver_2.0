from config import NOTION_DOMESTIC_STOCK_INFO_DB_ID
from notion.get_all_pages import get_all_pages

get_all_pages(NOTION_DOMESTIC_STOCK_INFO_DB_ID)

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
