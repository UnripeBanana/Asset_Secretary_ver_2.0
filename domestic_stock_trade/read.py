def read_domestic_stock_trade(page):

	props = page["properties"]

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

