def solution(my_string):
    data = my_string.replace(' - ',' + -').split(' + ')
    return sum([int(i.strip()) for i in data])