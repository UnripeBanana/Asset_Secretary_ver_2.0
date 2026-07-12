from utils.day_log import today_is
import pandas as pd

def append_krx_gold_history(df, krx_gold_info):
    #{'ticker': 'M04020000', 'name': '국내 금', 'price': 198270, 'change': 460, 'rate': 0.23, 'direction': '2', 'open_price': '199,680', 'high': '199,860', 'low': '198,250', 'volume': '134,123', 'value': '26,711백만'}

    row = {
        "date": str(today_is()),
        "ticker": str(krx_gold_info["ticker"]).zfill(6),
        "name": krx_gold_info["name"],
        "open": krx_gold_info["open_price"],
        "high": krx_gold_info["high"],
        "low": krx_gold_info["low"],
        "close": krx_gold_info["close_price"],
        "volume": krx_gold_info["volume"],
        "amount": krx_gold_info["value"],
    }




    return {
        "ticker": gold["symbolCode"],                                # 'M04020000'
        "name": gold["name"],                                        # 이름 : "국내 금"
        "price": int(gold["closePrice"].replace(",", "")),           # 현재가
        "change": int(gold["fluctuations"].replace(",", "")),        # 전일대비
        "rate": float(gold["fluctuationsRatio"]),                    # 등락률
        "direction": gold["fluctuationsType"]["code"],               # 등락여부
        "open_price": gold["openPrice"],                             # 시가
        "high": gold["highPrice"],                                   # 고가
        "low": gold["lowPrice"],                                     # 저가
        "close_price": gold["closePrice"],                           # 종가
        "volume": gold["accumulatedTradingVolume"],                  # 거래량
        "value": gold["accumulatedTradingValue"]                     # 거래대금
    }


    


def append_history(df, domestic_stock_info):
    row = {
        "date": str(today_is()),
        "ticker": str(domestic_stock_info["cd"]).zfill(6),
        "name": domestic_stock_info["nm"],
        "open": domestic_stock_info["ov"],
        "high": domestic_stock_info["hv"],
        "low": domestic_stock_info["lv"],
        "close": domestic_stock_info["nv"],
        "volume": domestic_stock_info["aq"],
        "amount": domestic_stock_info["aa"],
    }

    # 잠시 추가한 코드
    print("새로 추가할 row")
    print(row)
    
    print("\n삭제 대상")
    print(
        df[
            (df["date"] == row["date"]) &
            (df["ticker"] == row["ticker"])
        ]
    )
    
    # 같은 날짜 + 같은 티커 제거
    df = df[
        ~(
            (df["date"] == row["date"]) &
            (df["ticker"] == row["ticker"])
        )
    ]
    
    df = pd.concat(
        [df, pd.DataFrame([row])],
        ignore_index=True
    )

    return df
