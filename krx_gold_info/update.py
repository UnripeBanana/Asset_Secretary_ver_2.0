from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from notion.rich_text import rich_text
from utils.day_log import today_and_time_is
from domestic_stock_info.csv.get_high_low_nMonth import get_high_low_nMonth
from domestic_stock_info.update import update_nMonth_high_low_value

def update_krx_gold_info_DB(page, krx_gold_info):
    


    



        return {
        "price": int(gold["closePrice"].replace(",", "")),           # 현재가
        "change": int(gold["fluctuations"].replace(",", "")),        # 전일대비
        "rate": float(gold["fluctuationsRatio"]),                    # 등락률
        "direction": gold["fluctuationsType"]["name"],               # 등락여부
        "open_price": gold["openPrice"],                             # 시가
        "high": gold["highPrice"],                                   # 고가
        "low": gold["lowPrice"],                                     # 저가
        "volume": gold["accumulatedTradingVolume"],                  # 거래량
        "value": gold["accumulatedTradingValue"]                     # 거래대금    
    }

    
    
    # KRX 시장 값_ 나중에 NXT 시장 값도 넣자
    cv = domestic_stock_info["cv"]
    cr = domestic_stock_info["cr"]
    # 하락이면 음수로 변경
    if domestic_stock_info["rf"] == "5":
        cv *= -1
        cr *= -1
    
    # 3개월, 12개월 최고가 최저가 계산
    # update_nMonth_max_min_value(current_max, current_min, ticker, month)
    
    high_low_3m = update_nMonth_high_low_value(page, domestic_stock_info["hv"], domestic_stock_info["lv"], domestic_stock_info["cd"], 3)
    high_low_12m = update_nMonth_high_low_value(page, domestic_stock_info["hv"], domestic_stock_info["lv"], domestic_stock_info["cd"], 12)
    high_low_36m = update_nMonth_high_low_value(page, domestic_stock_info["hv"], domestic_stock_info["lv"], domestic_stock_info["cd"], 36)
    high_low_60m = update_nMonth_high_low_value(page, domestic_stock_info["hv"], domestic_stock_info["lv"], domestic_stock_info["cd"], 60)
    high_low_120m = update_nMonth_high_low_value(page, domestic_stock_info["hv"], domestic_stock_info["lv"], domestic_stock_info["cd"], 120)
        
    krx_domestic_stock_info_naver_finance = {
        # KRX 시장 값을 반환
    
        "현재가_깃허브": {"number": domestic_stock_info["nv"]},
        "전일대비_깃허브": {"number": cv},
        "등락률_깃허브": {"number": cr},
        "시가총액_깃허브": {"number": domestic_stock_info["nv"]*domestic_stock_info["countOfListedStock"]},
        "거래량_깃허브": {"number": domestic_stock_info["aq"]},
        "거래대금_깃허브": {"number": domestic_stock_info["aa"]},
        "3개월_최고가_깃허브": {"number": high_low_3m["high"]},
        "3개월_최저가_깃허브": {"number": high_low_3m["low"]},
        "12개월_최고가_깃허브": {"number": high_low_12m["high"]},
        "12개월_최저가_깃허브": {"number": high_low_12m["low"]},
        "36개월_최고가_깃허브": {"number": high_low_36m["high"]},
        "36개월_최저가_깃허브": {"number": high_low_36m["low"]},
        "60개월_최고가_깃허브": {"number": high_low_60m["high"]},
        "60개월_최저가_깃허브": {"number": high_low_60m["low"]},
        "120개월_최고가_깃허브": {"number": high_low_120m["high"]},
        "120개월_최저가_깃허브": {"number": high_low_120m["low"]},
        "마지막 업데이트": rich_text(today_and_time_is())
    }

    notion.pages.update(
        page_id = page["id"],
        properties = krx_domestic_stock_info_naver_finance
    )




def update_nMonth_high_low_value(page, current_high, current_low, ticker, month):
    # get_high_low_nMonth(ticker, month)
    high_low = get_high_low_nMonth(ticker, month)

    high_notion_text = f"{month}개월_최고가_깃허브"
    low_notion_text = f"{month}개월_최저가_깃허브"
    
    high = high_low["high"]
    low = high_low["low"]
    if high is None or current_high > high:
        high = current_high
    if low is None or current_low < low:
        low = current_low
    
    saved_high = page["properties"][high_notion_text]["number"]
    saved_low = page["properties"][low_notion_text]["number"]
    if saved_high is not None and saved_high > high:
        high = saved_high
    if saved_low is not None and saved_low < low:
        low = saved_low

    return {"high": high, "low": low}


  
  
# 노션에 쓰는 함수만 넣는다.

from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from notion.rich_text import rich_text
from utils.logger import logging
from config import NOTION_KRX_GOLD_INFO_DB_ID

def update_KRX_GOLD_INFO_DB(page, gold_info):

  price = gold_info["price"]
  change = gold_info["change"]
  rate = gold_info["rate"]
  direction = gold_info["direction"]
  
  # 하락이면 음수로 변경
  if direction == "FALLING":
    change = -change
    rate = -rate
  elif direction == "UNCHANGED":
    change = 0
    rate = 0

  gold_info_mod = {
    "현재가_깃허브_원본": {
        "number": price
    },
    "전일대비_깃허브_원본": {
        "number": change
    },
    "등락률_깃허브_원본": {
        "number": rate
    },
    "마지막 업데이트": rich_text(logging())
  } 
    
  notion.pages.update(
      page_id=page["id"],
      properties=gold_info_mod
  )



  
