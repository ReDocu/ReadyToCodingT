def solution(s):

    words = s.split(' ')
    
    add_num = 0
    add_sum = 0
    for word in words:
        if word == 'Z':
            add_sum = add_sum - add_num
            continue

        add_num = int(word)
        
        add_sum += add_num
    
    return add_sum