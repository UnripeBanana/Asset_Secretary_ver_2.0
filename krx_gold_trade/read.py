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

{'보유량': {'id': '%3BApQ', 'type': 'formula', 'formula': {'type': 'number', 'number': 1}}, '전일대비': {'id': '%3EW%3FY', 'type': 'formula', 'formula': {'type': 'string', 'string': '▲ 2,590'}}, '현재가_깃허브': {'id': 'AArF', 'type': 'number', 'number': 195680}, '등락률': {'id': 'GSZ%5D', 'type': 'formula', 'formula': {'type': 'string', 'string': '▲ 1.31%'}}, '마지막 업데이트': {'id': 'I%7B%7DL', 'type': 'rich_text', 'rich_text': [{'type': 'text', 'text': {'content': '2026-07-13 13:59', 'link': None}, 'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'default'}, 'plain_text': '2026-07-13 13:59', 'href': None}]}, '120개월_최고가_깃허브': {'id': 'NGDs', 'type': 'number', 'number': 256728}, '60개월_최고가_깃허브': {'id': 'O%3BOB', 'type': 'number', 'number': 256728}, '현재가': {'id': 'OZAj', 'type': 'formula', 'formula': {'type': 'string', 'string': '▲ 195,680'}}, '등락률_깃허브': {'id': 'Q~JD', 'type': 'number', 'number': 1.31}, '3개월_최고가_깃허브': {'id': 'SgSY', 'type': 'number', 'number': 229047}, '12개월_최저가_깃허브': {'id': '%5BvsZ', 'type': 'number', 'number': 146755}, '보유량_원본': {'id': '%5DAJf', 'type': 'rollup', 'rollup': {'type': 'number', 'number': 1, 'function': 'sum'}}, '120개월_최저가_깃허브': {'id': '%60XV_', 'type': 'number', 'number': 42148}, '거래량_깃허브': {'id': 'aMzw', 'type': 'number', 'number': 171367}, '매입금액': {'id': 'er%3FH', 'type': 'formula', 'formula': {'type': 'number', 'number': 202660}}, '60개월_최저가_깃허브': {'id': 'lAbX', 'type': 'number', 'number': 62196}, '12개월_최고가_깃허브': {'id': 'm%3CBd', 'type': 'number', 'number': 246320}, '매입금액_원본': {'id': 'm%5CNh', 'type': 'rollup', 'rollup': {'type': 'number', 'number': 202660, 'function': 'sum'}}, '36개월_최고가_깃허브': {'id': 'o%3FXY', 'type': 'number', 'number': 256727.59}, '거래대금_깃허브': {'id': 'ox_S', 'type': 'rich_text', 'rich_text': [{'type': 'text', 'text': {'content': '33,650백만', 'link': None}, 'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'default'}, 'plain_text': '33,650백만', 'href': None}]}, 'KRX 금현물 보유현황 DB ver 2.0': {'id': 'qOh%5C', 'type': 'relation', 'relation': [{'id': '2136e5ae-e083-825c-a01c-01baa595b197'}], 'has_more': False}, '36개월_최저가_깃허브': {'id': 'twIc', 'type': 'number', 'number': 78787}, '전일대비_깃허브': {'id': 'wDvJ', 'type': 'number', 'number': 2590}, 'KRX 금현물 거래내역 DB': {'id': 'x%3DSu', 'type': 'relation', 'relation': [{'id': '2606e5ae-e083-8246-8c85-01c8ba3edd53'}], 'has_more': False}, '3개월_최저가_깃허브': {'id': 'yGS%60', 'type': 'number', 'number': 195670}, '이름': {'id': 'title', 'type': 'title', 'title': [{'type': 'text', 'text': {'content': 'KRX 금현물', 'link': None}, 'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'default'}, 'plain_text': 'KRX 금현물', 'href': None}]}}
	
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
