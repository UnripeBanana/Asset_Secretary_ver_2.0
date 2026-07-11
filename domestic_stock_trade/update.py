from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할

def update_domestic_stock_trade_DB(results):
    for id in list(results.keys()):
        raw_prop = results[id]  # dict
        properties = {
            "잔량": {"number": raw_prop["remaining"]},
            "실현수익": {"number": raw_prop["profit"]}
        }

        notion.pages.update(
            page_id = id,
            properties = properties
        )
