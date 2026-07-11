from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from notion.rich_text import rich_text
from utils.logger import logging

def update_domestic_stock_info_DB(page, domestic_stock_info):

    # KRX 시장 값
    cv = domestic_stock_info["cv"]
    cr = domestic_stock_info["cr"]
    # 하락이면 음수로 변경
    if domestic_stock_info["rf"] == "5":
        cv *= -1
        cr *= -1

    # NXT 시장 값
    compareToPreviousClosePrice = domestic_stock_info["compareToPreviousClosePrice"]
    fluctuationsRatio = domestic_stock_info["fluctuationsRatio"]
    # 하락이면 음수로 변경
    if domestic_stock_info["compareToPreviousPrice"] == "5" and not domestic_stock_info["overPrice"]:
        compareToPreviousClosePrice *= -1
        fluctuationsRatio *= -1
        
    krx_domestic_stock_info_naver_finance = {
        # KRX 시장 값을 반환
    
        "현재가_깃허브": {"number": domestic_stock_info["nv"]},
        "전일대비_깃허브": {"number": cv},
        "등락률_깃허브": {"number": cr},
        "시가총액_깃허브": {"number": domestic_stock_info["nv"]*domestic_stock_info["countOfListedStock"]},
        "거래량_깃허브": {"number": domestic_stock_info["aq"]},
        "거래대금_깃허브": {"number": domestic_stock_info["aa"]},
        "마지막 업데이트": rich_text(logging())
    }
    return krx_domestic_stock_info_naver_finance

# NXT 시장 데이터 활용은 나중에 어느정도 코드가 완성됐을 때 추가하자
"""
    domestic_stock_info_naver_finance = {
        # NXT 시장 값을 반환
    
        "현재가_깃허브": {
            "number": domestic_stock_info["nv"]
        },
        "전일대비_깃허브": {
            "number": cv
        },
        "등락률_깃허브_원본": {
            "number": cr
        },
        "시가총액_깃허브": {
            "number": domestic_stock_info["nv"]*domestic_stock_info["countOfListedStock"]
    }
"""

        "nv": krx_item["nv"],      # 현재가
        "cv": krx_item["cv"],      # 전일 대비 가격 변화(원)
        "cr": krx_item["cr"],      # 등락률(%)
        "rf": krx_item["rf"],      # 등락 구분(2:상승/3:보합/5:하락을 나타내는 코드)
        "ms": krx_item["ms"],      # 장상태(OPEN/CLOSE)
        "pcv": krx_item["pcv"],    # Previous Close Value, 전일종가
        "ov": krx_item["ov"],      # 시가
        "hv": krx_item["hv"],      # 고가
        "lv": krx_item["lv"],      # 저가
        "aq": krx_item["aq"],      # 거래량
        "aa": krx_item["aa"],      # 거래대금 : 하루동안 얼마가 거래되었는가 (평균 거래대금보다 많은 양이 거래될 시 신뢰도 있는 등락이라고 판단)
        "countOfListedStock": krx_item["countOfListedStock"],  # 상장주식수

        # nxtOverMarketPriceInfo
        "overMarketStatus ": nxt_item["overMarketStatus "],      # 시간외 장 상태
        "overPrice": nxt_item["overPrice"],                      # 시간외 현재가
        "openPrice": nxt_item["openPrice"],                      # 시간외 시가 
        "highPrice": nxt_item["highPrice"],                      # 시간외 고가
        "lowPrice": nxt_item["lowPrice"],                        # 시간외 저가
        "compareToPreviousPrice": nxt_item["compareToPreviousPrice"],                  # 상승/하락 'compareToPreviousPrice': {'code': '2', 'text': '상승', 'name': 'RISING'}
        "compareToPreviousClosePrice": nxt_item["compareToPreviousClosePrice"],        # 전일대비
        "fluctuationsRatio": nxt_item["fluctuationsRatio"],                            # 등락률
        "accumulatedTradingVolume": nxt_item["accumulatedTradingVolume"],              # 거래량
        "accumulatedTradingValue": nxt_item["accumulatedTradingValue"]                 # 거래대금
