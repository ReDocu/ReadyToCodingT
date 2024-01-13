def solution(common):
    check2 = common[2] - common[1]
    check1 = common[1] - common[0]
    
    if check1 == check2:    # 등차수열
        return (common[-1] + check1)
    else:
        return (common[-1] * common[1]//common[0])
