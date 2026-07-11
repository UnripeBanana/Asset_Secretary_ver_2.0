from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from notion.rich_text import rich_text
from utils.day_log import today_is
from domestic_stock_info.csv.get_max_min_nMonth import get_max_min_nMonth

def update_domestic_stock_info_DB(page, domestic_stock_info):

    # KRX 시장 값_ 나중에 NXT 시장 값도 넣자
    cv = domestic_stock_info["cv"]
    cr = domestic_stock_info["cr"]
    # 하락이면 음수로 변경
    if domestic_stock_info["rf"] == "5":
        cv *= -1
        cr *= -1

    def get_ticker(page):
    ticker_data = page["properties"]["티커"]["rich_text"]
    if not ticker_data:
        return None
    return ticker_data[0]["plain_text"]
    
    # 3개월 최고가 최저가 계산
    _3month_max_min = get_max_min_nMonth(domestic_stock_info["cd"], 3)
    max_3 = _3month_max_min["high"]
    min_3 = _3month_max_min["low"]
    if domestic_stock_info["nv"] > max_3:
        max_3 = domestic_stock_info["nv"]
    if domestic_stock_info["nv"] < min_3:
        min_3 = domestic_stock_info["nv"]

    # 1년 최고가 최저가 계산
        
    krx_domestic_stock_info_naver_finance = {
        # KRX 시장 값을 반환
    
        "현재가_깃허브": {"number": domestic_stock_info["nv"]},
        "전일대비_깃허브": {"number": cv},
        "등락률_깃허브": {"number": cr},
        "시가총액_깃허브": {"number": domestic_stock_info["nv"]*domestic_stock_info["countOfListedStock"]},
        "거래량_깃허브": {"number": domestic_stock_info["aq"]},
        "거래대금_깃허브": {"number": domestic_stock_info["aa"]},
        "마지막 업데이트": rich_text(today_and_time_is())
    }

    notion.pages.update(
        page_id = page["id"],
        properties = krx_domestic_stock_info_naver_finance
    )
