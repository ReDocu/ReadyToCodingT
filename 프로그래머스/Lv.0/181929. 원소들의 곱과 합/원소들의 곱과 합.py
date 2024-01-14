def solution(num_list):
    
    check = 1
    for i in num_list:
        check *= i
    
    return 0 if check > sum(num_list) ** 2 else 1