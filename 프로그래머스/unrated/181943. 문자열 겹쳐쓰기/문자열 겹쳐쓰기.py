def solution(my_string, overwrite_string, s):
    
    result = list(my_string)
    
    for i in range(len(overwrite_string)):
        result[s + i] = overwrite_string[i]
    
    
    return ''.join(result)