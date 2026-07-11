from config import NOTION_DOMESTIC_STOCK_INFO_DB_ID
from notion.get_all_pages import get_all_pages
from history.main import domestic_stock_history_main


def main():
    pages = get_all_pages(NOTION_DOMESTIC_STOCK_INFO_DB_ID)
    domestic_stock_history_main(pages)

if __name__ == "__main__":
    main()
