# 네이버 증권에서 정보를 받아오기 위해 필요한 함수들 정리

import requests            # 네이버 증권에서 데이터 받아오기

# 국내주식 정보를 받아오기 위한 함수
def put_ticker_to_get_naver_prop(ticker):

    # 네이버는 브라우저가 아닌 프로그램의 요청을 차단하는 경우가 있어서, 브라우저인 척 속이는 역할 수행
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = (
        f"https://polling.finance.naver.com/api/realtime"
        f"?query=SERVICE_ITEM:{ticker}"
    )

    data = requests.get(
        url,
        headers=headers,
        timeout=10 # 최대 10초까지만 기다리겠다는 의미.
    ).json()

    krx_item = data["result"]["areas"][0]["datas"][0]
    nxt_item = data["result"]["areas"][0]["datas"][0]["nxtOverMarketPriceInfo"]

    # 임시로 넣은 코드
    import json
    print(json.dumps(item, indent=4, ensure_ascii=False))
  
    return {
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
    }
