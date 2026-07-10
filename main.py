from config import NOTION_DOMESTIC_STOCK_INFO_DB_ID
from notion.get_all_pages import get_all_pages

domestic_stock_main(get_all_pages(NOTION_DOMESTIC_STOCK_INFO_DB_ID))

    for page in pages:
        ticker = get_ticker(page)
