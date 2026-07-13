from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할

def read_krx_gold_trade(page):

	props = page["properties"]

	"""
	{'순수익 반영': {'id': '%3Cjg%5C', 'type': 'checkbox', 'checkbox': False}, '종목': {'id': 'C%7C~P', 'type': 'relation', 'relation': [{'id': '41c6e5ae-e083-8295-a848-0150faf1fe73'}], 'has_more': False}, 
	 '거래량 (g)': {'id': 'IwHm', 'type': 'number', 'number': 1}, '1g 당 가격': {'id': 'Zj%5CI', 'type': 'number', 'number': 202660}, '날짜': {'id': '%5E%60%5D%7B', 'type': 'date', 'date': {'start': '2026-07-07', 
	'end': None, 'time_zone': None}}, '실현수익': {'id': '_rWL', 'type': 'number', 'number': None}, '거래금액': {'id': '%60J%5C%7C', 'type': 'formula', 'formula': {'type': 'number', 'number': 202660}}, 
	 '잔량': {'id': 'e%7Bwy', 'type': 'number', 'number': None}, '매수/매도': {'id': 'jvTL', 'type': 'select', 'select': {'id': 'b6d0591e-973f-4d8e-baf4-35f8da7c2155', 'name': '매수', 'color': 'blue'}}, 
	 '': {'id': 'title', 'type': 'title', 'title': []}}
	 """

	relation_page_id = props["종목"]["relation"][0]["id"]
	relation_page = notion.pages.retrieve(relation_page_id)
	print(relation_page["properties"])

	
	"""
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
