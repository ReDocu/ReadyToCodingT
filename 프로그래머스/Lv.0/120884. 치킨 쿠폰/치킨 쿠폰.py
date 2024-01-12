def solution(chicken):
    
    sub = 0
    while chicken >= 10:
        sub += round(chicken/10)
        chicken /= 10
    
    
    return sub