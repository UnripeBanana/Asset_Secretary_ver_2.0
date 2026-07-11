from pathlib import Path
import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo

CSV_PATH = Path("domestic_stock_info/history/price_history.csv")

def create_csv():
    if CSV_PATH.exists():
        return

    columns = [
        "date",
        "ticker",
        "name",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "amount",
    ]

    pd.DataFrame(columns=columns).to_csv(
        CSV_PATH,
        index=False,
        encoding="utf-8-sig"
    )

def append_history(domestic_stock_info):
    row = {
        "date": datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d"),
        "ticker": domestic_stock_info["cd"],
        "name": domestic_stock_info["nm"],
        "open": domestic_stock_info["ov"],
        "high": domestic_stock_info["hv"],
        "low": domestic_stock_info["lv"],
        "close": domestic_stock_info["nv"],
        "volume": domestic_stock_info["aq"],
        "amount": domestic_stock_info["aa"],
    }

    df = pd.read_csv(CSV_PATH)
    df.loc[len(df)] = row
    df.to_csv(
        CSV_PATH,
        index=False,
        encoding="utf-8-sig"
    )
