def solution(price):
    if price >= 500000:
        answer = price - (price*0.2)
    elif price >= 300000:
        answer = price - (price * 0.1)
    elif price >= 100000:
        answer = price - (price * 0.05)
    else:
        return price
    
    return answer