def solution(num_list):
    even = [ x for x in num_list if x % 2 == 0]
    odd = [ x for x in num_list if x % 2 == 1]

    return [len(even),len(odd)]