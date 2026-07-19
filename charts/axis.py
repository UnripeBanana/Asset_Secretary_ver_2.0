def set_axis(ax, stock):
    # 위/오른쪽 테두리 제거
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    
    # y축을 오른쪽으로 이동
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    
    # 오른쪽 spine만 표시
    ax.spines["right"].set_visible(True)
    
    ax.tick_params(
        axis="y",
        left=False,
        labelleft=False,
        right=True,
        labelright=True
    )
    
    ax.set_xlim(-1, len(stock) + 6)
    
    # 여백 조금 주기
    price_min = stock["low"].min()
    price_max = stock["high"].max()
    
    margin = (price_max - price_min) * 0.05
    
    
    # y축을 0부터 보이게 설정
    ax.set_ylim(
        bottom = price_min - margin,
        top = price_max + margin
    )
    
    
    ax.set_ylim(
        price_min - margin,
        price_max + margin
    )
