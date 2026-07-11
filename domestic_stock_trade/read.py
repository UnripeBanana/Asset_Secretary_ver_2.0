from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from collections import defaultdict, deque

def read_domestic_stock_trade(page):

	props = page["properties"]

	trade = {
		"page_id": page["id"],
		"ticker": (props["종목명"]["select"]["name"] if props["종목명"]["select"] else None),
		"type": props["매수/매도"]["select"]["name"],
		"date": props["날짜"]["date"]["start"],
		"qty": props["수량"]["number"],
		"price": props["단가"]["number"],
		"amount": props["거래금액"]["formula"]["number"]
	}
	
	return trade

def group_by_ticker(trades):
    grouped = defaultdict(list)

    for trade in trades:
        grouped[trade["ticker"]].append(trade)

    return grouped
	
{'object': 'page', 'id': '0c36e5ae-e083-82aa-9ebd-81b77c0aeaaa', 'created_time': '2026-07-10T11:43:00.000Z', 'last_edited_time': '2026-07-10T11:43:00.000Z', 'created_by': 
 {'object': 'user', 'id': '6507eaf1-f105-4087-a20f-cb78ead8701b'}, 'last_edited_by': {'object': 'user', 'id': '6507eaf1-f105-4087-a20f-cb78ead8701b'}, 'cover': None, 'icon': None, 
 'parent': {'type': 'database_id', 'database_id': '4006e5ae-e083-82f1-9db7-8126271e8ac0'}, 'in_trash': False, 'is_archived': False, 'is_locked': False, 'properties': 
 {'실현수익': {'id': 'MtRP', 'type': 'number', 'number': None}, '잔량': {'id': 'Xh%60%60', 'type': 'number', 'number': 1}, '국내장 종목 DB': {'id': 'Z%3A%3C%3A', 'type': 'relation', 'relation': 
[{'id': 'b476e5ae-e083-8264-b74a-01dc0b69f7d6'}], 'has_more': False}, '매수/매도': {'id': '%5EZTK', 'type': 'select', 'select': {'id': '9c40e660-228c-4cdb-9231-56e7d76cc3e8', 'name': '매수', 'color': 'blue'}}, 
  '종목명': {'id': 'hrkg', 'type': 'select', 'select': {'id': '8b05d8ec-8e24-4455-87b6-6a70c1cd3b1c', 'name': '셀트리온', 'color': 'green'}}, '거래금액': {'id': 'jvLm', 'type': 'formula', 'formula': 
{'type': 'number', 'number': 171000}}, '보유량_금액': {'id': 'vnQ%5B', 'type': 'formula', 'formula': {'type': 'number', 'number': 171000}}, '수익 발생?': {'id': '%7DEug', 'type': 'relation', 'relation': [], 
'has_more': False}, '거래이유': {'id': 'title', 'type': 'title', 'title': [{'type': 'text', 'text': {'content': '평균 단가 낮추기.', 'link': None}, 'annotations': {'bold': False, 'italic': False, 'strikethrough': 
False, 'underline': False, 'code': False, 'color': 'default'}, 'plain_text': '평균 단가 낮추기.', 'href': None}]}, '단가': {'id': '256accfa-b8ba-4c78-9483-3d7d880ba315', 'type': 'number', 'number': 171000}, 
'목적': {'id': '4e836e73-2600-4060-a140-c02e37aa5cc6', 'type': 'multi_select', 'multi_select': [{'id': 'ececb3a8-fde4-47b4-9d1e-d0cdf33b212a', 'name': '장기투자', 'color': 'green'}]}, 
  '수량': {'id': 'ea529078-7025-4d5a-8299-006c9bfd8293', 'type': 'number', 'number': 1}, '날짜': {'id': 'f5771313-d3f7-4add-aa18-0eda24c23576', 'type': 'date', 'date': 
{'start': '2026-06-19', 'end': None, 'time_zone': None}}}, 'url': 'https://app.notion.com/p/0c36e5aee08382aa9ebd81b77c0aeaaa', 'public_url': 'https://enchanting-snowshoe-869.notion.site/0c36e5aee08382aa9ebd81b77c0aeaaa',
'archived': False}

