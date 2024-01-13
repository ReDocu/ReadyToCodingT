def solution(num, total):

    x = 0
    for i in range(1, num):
        x += i
        
    y = (total - x)//num
    
    return [i for i in range(y, y+num)]