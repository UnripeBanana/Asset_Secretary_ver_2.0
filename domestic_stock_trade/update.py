from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할

def update_trade_page(page_id, remaining=None, profit=None):



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

{'e816e5ae-e083-836a-9f48-01e15f18cd77': {'ticker': '한온시스템', 'date': '2026-06-18', 'remaining': 1}, '4536e5ae-e083-83b1-8c3b-01c3b189dd2e': {'ticker': '한온시스템', 'date': '2026-06-19', 'remaining': 1}, '2cd6e5ae-e083-82d4-b6f1-010dd93d32a6': {'ticker': '한온시스템', 'date': '2026-06-19', 'remaining': 1}, '6a36e5ae-e083-8318-962f-81a852d29d56': {'ticker': '한온시스템', 'date': '2026-06-19', 'remaining': 1}, 'f0b6e5ae-e083-83c1-90ec-817e7c61a1af': {'ticker': '한온시스템', 'date': '2026-06-23', 'remaining': 1}, '1d06e5ae-e083-8302-9b65-019a0b4626d9': {'ticker': '한온시스템', 'date': '2026-07-09', 'remaining': 1}, '2d76e5ae-e083-83da-9436-01f0fcd193fd': {'ticker': '카카오', 'date': '2025-10-29', 'remaining': 1}, '2566e5ae-e083-823b-8c8e-818f59e49b20': {'ticker': '카카오', 'date': '2025-10-30', 'remaining': 1}, '5586e5ae-e083-8378-897b-817f69526ba6': {'ticker': '카카오', 'date': '2025-10-30', 'remaining': 1}, '5a86e5ae-e083-83fd-9e86-01571d141789': {'ticker': '카카오', 'date': '2025-11-04', 'remaining': 1}, '4616e5ae-e083-8266-b1a3-81471ba0a234': {'ticker': '카카오', 'date': '2025-11-05', 'remaining': 3}, '7e96e5ae-e083-839b-81f9-0119887e0022': {'ticker': '카카오', 'date': '2025-11-05', 'remaining': 2}, 'b216e5ae-e083-826d-a451-019b677d1c97': {'ticker': '카카오', 'date': '2025-11-05', 'remaining': 4}, '1b56e5ae-e083-83ad-a7d8-01195047e0f5': {'ticker': '카카오', 'date': '2025-11-06', 'remaining': 4}, 'a496e5ae-e083-8310-8fa4-811e5c0f3b48': {'ticker': '카카오', 'date': '2025-11-06', 'remaining': 1}, '87d6e5ae-e083-833b-af62-812320df7390': {'ticker': '셀트리온', 'date': '2026-06-16', 'remaining': 1}, '0c36e5ae-e083-82aa-9ebd-81b77c0aeaaa': {'ticker': '셀트리온', 'date': '2026-06-19', 'remaining': 1}, '9786e5ae-e083-821c-94fc-817b6052fc8e': {'ticker': '현대차우', 'date': '2026-05-18', 'remaining': 1}, '4796e5ae-e083-82d6-a2f6-812b00b8ec95': {'ticker': '현대차우', 'date': '2026-06-11', 'remaining': 1}, 'daf6e5ae-e083-8365-92de-018d0273fde2': {'ticker': '현대차우', 'date': '2026-06-18', 'remaining': 1}, '9056e5ae-e083-8388-9990-8184d4f03e5c': {'ticker': '현대차우', 'date': '2026-06-18', 'remaining': 1}, 'a7f6e5ae-e083-8375-ad66-01561aa7b823': {'ticker': '현대차', 'date': '2026-06-17', 'remaining': 1}, '59f6e5ae-e083-8321-9732-810d08476cc8': {'ticker': '현대차', 'date': '2026-07-08', 'remaining': 1}, '9076e5ae-e083-8217-a832-817a57e0487d': {'ticker': '삼성전자우', 'date': '2026-05-18', 'remaining': 0}, , '7f86e5ae-e083-8338-9c6a-81093f738890': {'ticker': '삼성전자우', 'date': '2026-06-19', 'remaining': 1}, '9446e5ae-e083-82af-83c7-81578d26b1bf': {'ticker': '삼성전자', 'date': '2026-06-19', 'remaining': 1}}
'2436e5ae-e083-82fb-84cc-015a2f17e27a': {'ticker': '삼성전자우', 'date': '2026-06-18', 'remaining': 0, 'profit': 55500}

def update_domestic_stock_trade_DB(results):
    for id in list(results.keys()):
        raw_prop = results[id]  # dict
        properties = {
            "현재가_깃허브": {"number": domestic_stock_info["nv"]},
            "잔량"
        }


        
        notion.pages.update(
            page_id = id,
            properties = krx_domestic_stock_info_naver_finance
        )
    
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
