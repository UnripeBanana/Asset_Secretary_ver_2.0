def update_krx_gold_info_DB(page, krx_gold_info):





  
    return {
        "price": int(gold["closePrice"].replace(",", "")),           # 현재가
        "change": int(gold["fluctuations"].replace(",", "")),        # 전일대비
        "rate": float(gold["fluctuationsRatio"]),                    # 등락률
        "direction": gold["fluctuationsType"]["name"],               # 등락여부
        "open_price": gold["openPrice"],                             # 시가
        "high": gold["highPrice"],                                   # 고가
        "low": gold["lowPrice"],                                     # 저가
        "volume": gold["accumulatedTradingVolume"],                  # 거래량
        "value": gold["accumulatedTradingValue"]                     # 거래대금    
    }
