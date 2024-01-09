def solution(my_string):
    result = list()
    for value in my_string:
        if value not in result:
            result.append(value)
    
    return ''.join(result)
