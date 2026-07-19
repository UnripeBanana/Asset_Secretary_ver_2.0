from notion.client import notion

def initialize_stock_page(page_id):

    notion.blocks.children.append(
        block_id=page_id,
        children=[

            # -------------------------
            # 3개월 차트
            # -------------------------
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "3개월 차트"
                            }
                        }
                    ]
                }
            },

            # -------------------------
            # 구분선
            # -------------------------
            {
                "object": "block",
                "type": "divider",
                "divider": {}
            },

            # -------------------------
            # 1년 차트
            # -------------------------
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "1년 차트"
                            }
                        }
                    ]
                }
            },

            # -------------------------
            # 구분선
            # -------------------------
            {
                "object": "block",
                "type": "divider",
                "divider": {}
            },

            # -------------------------
            # 투자 메모
            # -------------------------
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "투자 메모"
                            }
                        }
                    ]
                }
            }

        ]
    )
