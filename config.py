# 환경변수 모으기

import os

# 노션에 연결중인 현재가 DB의 토큰값.
NOTION_TOKEN = os.environ["NOTION_TOKEN"]

# 국내주식 종목 DB 링크
NOTION_DOMESTIC_STOCK_INFO_DB_ID = os.environ["NOTION_DOMESTIC_STOCK_INFO_DB_ID"]

# 순수익 DB 링크
NOTION_NET_PROFIT_DB_ID = os.environ["NOTION_NET_PROFIT_DB_ID"]
