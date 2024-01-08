def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def solution(n):
    
    for i in range(1,12):
        if n < factorial(i):
            return i - 1