from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from notion.rich_text import rich_text
from utils.day_log import today_and_time_is
from domestic_stock_info.csv.get_high_low_nMonth import get_high_low_nMonth

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


def update_domestic_stock_info_DB(page, domestic_stock_info):

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
        "마지막 업데이트": rich_text(today_and_time_is())
    }

    notion.pages.update(
        page_id = page["id"],
        properties = krx_domestic_stock_info_naver_finance
    )
