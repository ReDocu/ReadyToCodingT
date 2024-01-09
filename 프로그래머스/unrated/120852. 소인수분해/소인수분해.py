def solution(n):
    number = list()
    
    x = 2
    while x <= n:
        if n % x == 0:
            if x not in number:
                number.append(x)
            n //= x
        else:
            x += 1
    
    return number