from pathlib import Path
from datetime import datetime
import pandas as pd

CSV_PATH = Path("domestic_stock_info/csv/price_history.csv")

def get_max_min_nMonth(ticker: str, months: int) -> dict[str, int | None]:
    """
    특정 종목의 최근 N개월 최고가/최저가를 반환
    ticker : str 종목 코드 (예: "005930")
    months : int 조회 기간 (3 또는 12 등)
    """

    # CSV 읽기
    df = pd.read_csv(CSV_PATH)

    # 날짜 변환
    df["date"] = pd.to_datetime(df["date"])

    # 종목 필터
    df = df[df["ticker"] == ticker]

    if df.empty:
        return {
            "high": None,
            "low": None
        }

    # 최근 N개월
    start_date = pd.Timestamp.today().normalize() - pd.DateOffset(months=months)
    df = df[df["date"] >= start_date]

    if df.empty:
        return {
            "high": None,
            "low": None
        }

    return {
        "high": int(df["high"].max()),
        "low": int(df["low"].min())
    }
