from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from notion.rich_text import rich_text
from utils.day_log import today_is

def update_domestic_stock_info_DB(page, domestic_stock_info):

    # KRX 시장 값
    cv = domestic_stock_info["cv"]
    cr = domestic_stock_info["cr"]
    # 하락이면 음수로 변경
    if domestic_stock_info["rf"] == "5":
        cv *= -1
        cr *= -1

    # NXT 시장 값
    compareToPreviousClosePrice = domestic_stock_info["compareToPreviousClosePrice"]
    fluctuationsRatio = domestic_stock_info["fluctuationsRatio"]
    # 하락이면 음수로 변경
    if domestic_stock_info["compareToPreviousPrice"] == "5" and not domestic_stock_info["overPrice"]:
        compareToPreviousClosePrice *= -1
        fluctuationsRatio *= -1
        
    krx_domestic_stock_info_naver_finance = {
        # KRX 시장 값을 반환
    
        "현재가_깃허브": {"number": domestic_stock_info["nv"]},
        "전일대비_깃허브": {"number": cv},
        "등락률_깃허브": {"number": cr},
        "시가총액_깃허브": {"number": domestic_stock_info["nv"]*domestic_stock_info["countOfListedStock"]},
        "거래량_깃허브": {"number": domestic_stock_info["aq"]},
        "거래대금_깃허브": {"number": domestic_stock_info["aa"]},
        "마지막 업데이트": rich_text(today_is())
    }

    notion.pages.update(
        page_id = page["id"],
        properties = krx_domestic_stock_info_naver_finance
    )

# NXT 시장 데이터 활용은 나중에 어느정도 코드가 완성됐을 때 추가하자
"""
    domestic_stock_info_naver_finance = {
        # NXT 시장 값을 반환
    
        "현재가_깃허브": {
            "number": domestic_stock_info["nv"]
        },
        "전일대비_깃허브": {
            "number": cv
        },
        "등락률_깃허브_원본": {
            "number": cr
        },
        "시가총액_깃허브": {
            "number": domestic_stock_info["nv"]*domestic_stock_info["countOfListedStock"]
    }
"""
