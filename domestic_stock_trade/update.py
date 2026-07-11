from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할

def update_trade_page(page_id, remaining=None, profit=None):

    properties = {}

    if remaining is not None:
        properties["잔량"] = {
            "number": remaining
        }

    if profit is not None:
        properties["실현수익"] = {
            "number": profit
        }

    notion.pages.update(
        page_id=page_id,
        properties=properties
    )


def update_domestic_stock_trade_DB(results):

    
    
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
