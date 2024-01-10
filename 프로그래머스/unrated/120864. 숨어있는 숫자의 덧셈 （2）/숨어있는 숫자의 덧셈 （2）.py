def solution(my_string):
       
    temp_string = ''
    for i in my_string:
        if i.isdigit():
            temp_string += i
        else:
            temp_string += ' '

    return sum([int(i) for i in temp_string.split()])