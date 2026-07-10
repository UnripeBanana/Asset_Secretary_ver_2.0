from config import NOTION_DOMESTIC_STOCK_INFO_DB_ID
from notion.get_all_pages import get_all_pages

# get_all_pages(NOTION_DOMESTIC_STOCK_INFO_DB_ID)

# 네이버는 브라우저가 아닌 프로그램의 요청을 차단하는 경우가 있어서, 브라우저인 척 속이는 역할 수행
headers = {
    "User-Agent": "Mozilla/5.0"
}

url = (
    f"https://polling.finance.naver.com/api/realtime"
    f"?query=SERVICE_ITEM:{ticker}"
)

data = requests.get(
    url,
    headers=headers,
    timeout=10 # 최대 10초까지만 기다리겠다는 의미.
).json()

item = data["result"]["areas"][0]["datas"][0]


"""
pages = get_all_pages(NOTION_DOMESTIC_STOCK_INFO_DB_ID)

for page in pages:
    print(page)
    if page:
        break
##########################
domestic_stock_main(get_all_pages(NOTION_DOMESTIC_STOCK_INFO_DB_ID))

    for page in pages:
        ticker = get_ticker(page)

def get_ticker(page):
    ticker_data = page["properties"]["티커"]["rich_text"]

    if not ticker_data:
        return None

    return ticker_data[0]["plain_text"]
"""
