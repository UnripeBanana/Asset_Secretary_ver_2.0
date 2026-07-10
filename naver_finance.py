# 네이버 증권에서 정보를 받아오기 위해 필요한 함수들 정리

import requests            # 네이버 증권에서 데이터 받아오기

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

    item = data["result"]["areas"][0]["datas"][0]

    # 임시로 넣은 코드
    import json
    print(json.dumps(item, indent=4, ensure_ascii=False))
  
    return {
        "price": item["nv"],   # 현재가
        "change": item["cv"],  # 전일 대비 가격 변화(원)
        "rf": item["rf"],      # 등락 구분(상승/하락/보합을 나타내는 코드)
        "cr": item["cr"],      # 등락률(%)

        "open": item["ov"],
        "high": item["hv"],
        "low": item["lv"],
        "volume": item["aq"],
        
        "countOfListedStock": item["countOfListedStock"]  # 상장주식수
    }
