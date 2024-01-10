def solution(before, after):
    
    for i in set(before):
        if before.count(i) == after.count(i):
            continue
        else:
            return 0
    return 1
