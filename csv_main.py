from config import NOTION_DOMESTIC_STOCK_INFO_DB_ID, NOTION_KRX_GOLD_INFO_DB_ID
from notion.get_all_pages import get_all_pages
from pathlib import Path
import pandas as pd

"""
#-----------------------------------------
# 국내주식 CSV 업데이트
#-----------------------------------------
from domestic_stock_info.read import get_ticker
from domestic_stock_info.data import get_domestic_stock_info
from domestic_stock_info.csv.update import append_domestic_stock_history

DOMESTIC_STOCK_CSV_PATH = Path("domestic_stock_info/csv/price_history.csv")

domestic_stock_df = pd.read_csv(
    DOMESTIC_STOCK_CSV_PATH,
    dtype={"ticker": str}
)

for page in get_all_pages(NOTION_DOMESTIC_STOCK_INFO_DB_ID):
  # 티커 데이터 추출
  ticker = get_ticker(page)
  if not ticker:
      continue

  # 네이버증권에서 데이터 받아오기
  domestic_stock_info = get_domestic_stock_info(ticker) # dictionary
  
  # CSV에 데이터 업로드
  domestic_stock_df = append_domestic_stock_history(domestic_stock_df, domestic_stock_info)

domestic_stock_df.to_csv(
    DOMESTIC_STOCK_CSV_PATH,
    index=False,
    encoding="utf-8-sig"
)
"""
#-----------------------------------------
# KRX 금현물 CSV 업데이트
#-----------------------------------------
from krx_gold_info.data import get_krx_gold_info
from krx_gold_info.csv.update import append_krx_gold_history

KRX_GOLD_CSV_PATH = Path("krx_gold_info/csv/price_history.csv")

krx_gold_df = pd.read_csv(
    KRX_GOLD_CSV_PATH,
    dtype={"ticker": str}
)

for page in get_all_pages(NOTION_KRX_GOLD_INFO_DB_ID):
    # 네이버증권에서 데이터 받아오기
    krx_gold_info = get_krx_gold_info()

    # CSV에 데이터 업로드
    krx_gold_df = append_krx_gold_history(krx_gold_df, krx_gold_info)

krx_gold_df.to_csv(
    KRX_GOLD_CSV_PATH,
    index=False,
    encoding="utf-8-sig"
)

print(KRX_GOLD_CSV_PATH.resolve())
print(len(krx_gold_df))

pages = get_all_pages(NOTION_KRX_GOLD_INFO_DB_ID)
print("pages:", len(pages))

krx_gold_info = get_krx_gold_info()
print(krx_gold_info)
