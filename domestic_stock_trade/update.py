from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from net_profit import net_profit

def update_domestic_stock_trade_DB(results, trades):
    trade_map = {
        trade["page_id"]: trade
        for trade in trades
    }
    
    for id, raw_prop in results.items():
        properties = {
            "잔량": {"number": raw_prop["remaining"]},
            "실현수익": {"number": raw_prop["profit"]}
        }

        trade = trade_map[page_id]

        if raw_prop["profit"] and not trade["profit_saved"]: 
            net_profit("domestic_stock", raw_prop["profit"])

        notion.pages.update(
            page_id = id,
            properties = properties
        )
