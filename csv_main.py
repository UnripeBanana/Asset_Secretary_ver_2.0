from config import NOTION_DOMESTIC_STOCK_INFO_DB_ID
from notion.get_all_pages import get_all_pages

#-----------------------------------------
# 국내주식 CSV 업데이트
#-----------------------------------------
from domestic_stock_info.read import get_ticker
from domestic_stock_info.data import get_domestic_stock_info
from domestic_stock_info.csv.update import append_history

for page in get_all_pages(NOTION_DOMESTIC_STOCK_INFO_DB_ID):
  # 티커 데이터 추출
  ticker = get_ticker(page)
  if not ticker:
      continue

  # 네이버증권에서 데이터 받아오기
  domestic_stock_info = get_domestic_stock_info(ticker) # dictionary

  CSV_PATH = Path("domestic_stock_info/csv/price_history.csv")
  
  df = pd.read_csv(
      CSV_PATH,
      dtype={"ticker": str}
  )
  
  # CSV에 데이터 업로드
  append_history(df, domestic_stock_info)

  df.to_csv(
      CSV_PATH,
      index=False,
      encoding="utf-8-sig"
  )
