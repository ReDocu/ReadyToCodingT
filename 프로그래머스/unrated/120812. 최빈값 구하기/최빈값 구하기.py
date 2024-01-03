def solution(array):
    check_array = set(array)
    check_dict = dict()

    for item in check_array:
        check_dict[item] = array.count(item)

    return max(check_dict,key=check_dict.get) if list(check_dict.values()).count(max(check_dict.values())) <= 1 else -1