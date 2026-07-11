from pathlib import Path
import pandas as pd

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
