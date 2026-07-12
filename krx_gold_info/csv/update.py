from utils.day_log import today_is
import pandas as pd

def append_krx_gold_history(df, krx_gold_info):
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

