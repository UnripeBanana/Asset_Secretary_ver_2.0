from config import NOTION_PRICE_DB_ID, NOTION_TRADE_DB_ID, NOTION_KRX_GOLD_INFO_DB_ID, NOTION_KRX_GOLD_TRADE_DB_ID, NOTION_DOMESTIC_BOND_ETF_DB_ID
from notion.get_all_pages import get_all_pages

from domestic_stock.main import domestic_stock_main
from domestic_stock_trade.main import domestic_stock_trade_main
from gold.main import gold_main
from gold_trade.main import gold_trade_main
from domestic_bond_etf.main import domestic_bond_etf_DB_main

# 초기 개발 완료
#domestic_stock_main(get_all_pages(NOTION_PRICE_DB_ID))
#domestic_stock_trade_main(NOTION_TRADE_DB_ID)
#gold_main(get_all_pages(NOTION_KRX_GOLD_INFO_DB_ID))

# 개발 진행 중
gold_trade_main(NOTION_KRX_GOLD_TRADE_DB_ID)
#domestic_bond_etf_DB_main(get_all_pages(NOTION_DOMESTIC_BOND_ETF_DB_ID))
