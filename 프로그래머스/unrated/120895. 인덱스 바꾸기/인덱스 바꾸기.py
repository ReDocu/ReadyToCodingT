def solution(my_string, num1, num2):
    temp_string = list(my_string)
    temp = temp_string[num1]
    temp_string[num1] = temp_string[num2]
    temp_string[num2] = temp
    
    result = ''
    for i in temp_string:
        result += i
    
    return result