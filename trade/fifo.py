from collections import deque

{'e816e5ae-e083-836a-9f48-01e15f18cd77': {'remaining': 1}, '4536e5ae-e083-83b1-8c3b-01c3b189dd2e': {'remaining': 1}, '2cd6e5ae-e083-82d4-b6f1-010dd93d32a6': {'remaining': 1}, '6a36e5ae-e083-8318-962f-81a852d29d56': {'remaining': 1}, 'f0b6e5ae-e083-83c1-90ec-817e7c61a1af': {'remaining': 1}, '1d06e5ae-e083-8302-9b65-019a0b4626d9': {'remaining': 1}, '2d76e5ae-e083-83da-9436-01f0fcd193fd': {'remaining': 1}, '2566e5ae-e083-823b-8c8e-818f59e49b20': {'remaining': 1}, '5586e5ae-e083-8378-897b-817f69526ba6': {'remaining': 1}, '5a86e5ae-e083-83fd-9e86-01571d141789': {'remaining': 1}, '4616e5ae-e083-8266-b1a3-81471ba0a234': {'remaining': 3}, '7e96e5ae-e083-839b-81f9-0119887e0022': {'remaining': 2}, 'b216e5ae-e083-826d-a451-019b677d1c97': {'remaining': 4}, '1b56e5ae-e083-83ad-a7d8-01195047e0f5': {'remaining': 4}, 'a496e5ae-e083-8310-8fa4-811e5c0f3b48': {'remaining': 1}, '87d6e5ae-e083-833b-af62-812320df7390': {'remaining': 1}, '0c36e5ae-e083-82aa-9ebd-81b77c0aeaaa': {'remaining': 1}, '9786e5ae-e083-821c-94fc-817b6052fc8e': {'remaining': 1}, '4796e5ae-e083-82d6-a2f6-812b00b8ec95': {'remaining': 1}, 'daf6e5ae-e083-8365-92de-018d0273fde2': {'remaining': 1}, '9056e5ae-e083-8388-9990-8184d4f03e5c': {'remaining': 1}, 'a7f6e5ae-e083-8375-ad66-01561aa7b823': {'remaining': 1}, '59f6e5ae-e083-8321-9732-810d08476cc8': {'remaining': 1}, '9076e5ae-e083-8217-a832-817a57e0487d': {'remaining': 0}, '2436e5ae-e083-82fb-84cc-015a2f17e27a': {'remaining': 0, 'profit': 55500}, '7f86e5ae-e083-8338-9c6a-81093f738890': {'remaining': 1}, '9446e5ae-e083-82af-83c7-81578d26b1bf': {'remaining': 1}}

def process_fifo(grouped_trades):
    updates = {}

    for ticker, trades in grouped_trades.items():
        queue = deque()
        realized_profit = 0

        for trade in trades:
            page_id = trade["page_id"]

            # 페이지 정보가 없으면 생성
            if page_id not in updates:
                updates[page_id] = {}

            # -----------------
            # 매수
            # -----------------
            if trade["type"] == "매수":
                queue.append({
                    "page_id": page_id,
                    "qty": trade["qty"],
                    "price": trade["price"]
                })
                updates[page_id]["remaining"] = trade["qty"]

            # -----------------
            # 매도
            # -----------------
            else:
                sell_qty = trade["qty"]
                sell_profit = 0

                # 매도 페이지의 잔량은 항상 0
                updates[page_id]["remaining"] = 0

                while sell_qty > 0:
                    if not queue:
                        raise ValueError(
                            f"{ticker}의 보유수량보다 많은 매도가 발생했습니다."
                        )

                    oldest = queue[0]

                    matched = min(
                        sell_qty,
                        oldest["qty"]
                    )

                    profit = (
                        trade["price"] - oldest["price"]
                    ) * matched

                    realized_profit += profit
                    sell_profit += profit

                    oldest["qty"] -= matched
                    sell_qty -= matched

                    # 기존 매수 페이지 잔량 감소
                    updates[oldest["page_id"]]["remaining"] -= matched

                    if oldest["qty"] == 0:
                        queue.popleft()

                updates[page_id]["profit"] = sell_profit

    return updates
