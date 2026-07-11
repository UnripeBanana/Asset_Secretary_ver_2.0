from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from net_profit import net_profit

def update_domestic_stock_trade_DB(results):
    for id, raw_prop in results.items():
        properties = {
            "잔량": {"number": raw_prop["remaining"]},
            "실현수익": {"number": raw_prop["profit"]}
        }

        if raw_prop["profit"]: 
            net_profit("domestic_stock", raw_prop["profit"])

        notion.pages.update(
            page_id = id,
            properties = properties
        )
