def solution(i, j, k):
    
    return sum([str(check).count(str(k)) for check in range(i,j + 1)])