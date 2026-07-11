from config import NOTION_NET_PROFIT_DB_ID
from notion.client import notion

def net_profit(prop, profit):
    notion.pages.create(
        parent={
            "database_id": NOTION_NET_PROFIT_DB_ID
        },
        properties={
            "국내주식 수익": {"number": },
            "국내주식 배당금 수익": {"number": 10},
            "업데이트 일시": rich_text(today_and_time_is())
        }
    )
