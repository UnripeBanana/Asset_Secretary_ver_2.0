import pandas as pd
from utils.day_log import today_is

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
    
    df.loc[len(df)] = row

    return df

