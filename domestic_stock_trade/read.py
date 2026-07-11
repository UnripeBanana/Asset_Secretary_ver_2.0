def read_domestic_stock_trade(page):

	props = page["properties"]

#	print(props)
#	{'실현수익': {'id': 'MtRP', 'type': 'number', 'number': 0}, '잔량': {'id': 'Xh%60%60', 'type': 'number', 'number': 1}, , '매수/매도': {'id': '%5EZTK', 'type': 'select', 'select': {'id': '9c40e660-228c-4cdb-9231-56e7d76cc3e8', 'name': '매수', 'color': 'blue'}}, '종목명': {'id': 'hrkg', 'type': 'select', 'select': {'id': '9f9aab0a-05c1-4e90-b2ed-72f1ceb1c472', 'name': '한온시스템', 'color': 'pink'}}, '거래금액': {'id': 'jvLm', 'type': 'formula', 'formula': {'type': 'number', 'number': 4000}}, '보유량_금액': {'id': 'vnQ%5B', 'type': 'formula', 'formula': {'type': 'number', 'number': 4000}}, '거래이유': {'id': 'title', 'type': 'title', 'title': []}, '단가': {'id': '256accfa-b8ba-4c78-9483-3d7d880ba315', 'type': 'number', 'number': 4000}, '목적': {'id': '4e836e73-2600-4060-a140-c02e37aa5cc6', 'type': 'multi_select', 'multi_select': [{'id': 'b5eee916-03a5-4967-9fcd-36d2881e1129', 'name': '첫 1000% 수익률 목표', 'color': 'red'
#'국내장 종목 DB': {'id': 'Z%3A%3C%3A', 'type': 'relation', 'relation': [{'id': 'ef06e5ae-e083-8235-9667-81042e23f60b'}], 'has_more': False}

	relation_page_id = props["국내장 종목 DB"]["relation"][0]["id"]
	
	trade = {
		"page_id": page["id"],
		"ticker": (props["종목명"]["select"]["name"] if props["종목명"]["select"] else None),
		"type": props["매수/매도"]["select"]["name"],
		"date": props["날짜"]["date"]["start"],
		"qty": props["거래량"]["number"],
		"price": props["단가"]["number"],
		"amount": props["거래금액"]["formula"]["number"]
	}
	
	return trade

