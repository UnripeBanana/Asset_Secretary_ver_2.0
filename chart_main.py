import pandas as pd

df = pd.read_csv("domestic_stock_info/csv/price_history.csv")

# print(df.head())

ticker = "005930"

stock = df[df["ticker"] == ticker].copy()

stock["date"] = pd.to_datetime(stock["date"])

stock = stock.set_index("date")

print(stock.head())
