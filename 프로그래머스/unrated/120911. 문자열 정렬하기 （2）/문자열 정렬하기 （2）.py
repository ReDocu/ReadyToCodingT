def solution(my_string):
    
    msg = '' 
    for i in sorted(my_string.lower()):
        msg += i
    
    return msg