from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할

def read_dividend(page):
	props = page["properties"]

	properties = {
		"page_id": page["id"],
		"dividend": props["배당금"]["formula"]["number"],
		"profit_saved": props["순수익 반영"]["checkbox"]
	}

	return properties

{'object': 'page', 'id': '39b6e5ae-e083-8079-a9b9-dfbd015a9226', 'created_time': '2026-07-12T01:30:00.000Z', 'last_edited_time': '2026-07-12T01:31:00.000Z', 'created_by': {'object': 'user', 'id': '6507eaf1-f105-4087-a20f-cb78ead8701b'}, 'last_edited_by': {'object': 'user', 'id': '6507eaf1-f105-4087-a20f-cb78ead8701b'}, 'cover': None, 'icon': None, 'parent': {'type': 'database_id', 'database_id': '39b6e5ae-e083-80dc-981c-e11e5fc8dcf0'}, 'in_trash': False, 'is_archived': False, 'is_locked': False, 'properties': {'보유 주식량': {'id': '%3DEMG', 'type': 'number', 'number': 1}, '배당지급일': {'id': 'C%3E%3B%5E', 'type': 'date', 'date': {'start': '2026-06-30', 'end': None, 'time_zone': None}}, '순수익 반영': {'id': 'DMwN', 'type': 'checkbox', 'checkbox': False}, '1주당 배당금': {'id': 'i_ap', 'type': 'number', 'number': 2500}, '종목': {'id': 'kN%5D%7C', 'type': 'relation', 'relation': [{'id': '9056e5ae-e083-8329-af3f-81c82c3fbc00'}], 'has_more': False}, '배당금': {'id': 'om%60%40', 'type': 'formula', 'formula': {'type': 'number', 'number': 2500}}, ' ': {'id': 'title', 'type': 'title', 'title': []}}, 'url': 'https://app.notion.com/p/39b6e5aee0838079a9b9dfbd015a9226', 'public_url': 'https://enchanting-snowshoe-869.notion.site/39b6e5aee0838079a9b9dfbd015a9226', 'archived': False}
'properties': {'보유 주식량': {'id': '%3DEMG', 'type': 'number', 'number': 1}, '배당지급일': {'id': 'C%3E%3B%5E', 'type': 'date', 'date': {'start': '2026-06-30', 'end': None, 'time_zone': None}}, '순수익 반영': {'id': 'DMwN', 'type': 'checkbox', 'checkbox': False}, '1주당 배당금': {'id': 'i_ap', 'type': 'number', 'number': 2500}, '종목': {'id': 'kN%5D%7C', 'type': 'relation', 'relation': [{'id': '9056e5ae-e083-8329-af3f-81c82c3fbc00'}], 'has_more': False}, '배당금': {'id': 'om%60%40', 'type': 'formula', 'formula': {'type': 'number', 'number': 2500}}
'배당금': {'id': 'om%60%40', 'type': 'formula', 'formula': {'type': 'number', 'number': 2500}
"""
from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할

def read_domestic_stock_trade(page):

	props = page["properties"]

	relation_page_id = props["국내장 종목 DB"]["relation"][0]["id"]
	relation_page = notion.pages.retrieve(relation_page_id)
	
	trade = {
		"page_id": page["id"],
		"ticker": relation_page["properties"]["종목"]["title"][0]["plain_text"],
		"type": props["매수/매도"]["select"]["name"],
		"date": props["날짜"]["date"]["start"],
		"qty": props["거래량"]["number"],
		"price": props["단가"]["number"],
		"amount": props["거래금액"]["formula"]["number"],
		"profit_saved": props["순수익 반영"]["checkbox"]
	}
	
	return trade
  """
