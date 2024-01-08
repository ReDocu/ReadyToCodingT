def solution(babbling):
    words = ['aya','ye','woo','ma']
    
    count = 0
    for item in babbling:
        for word in words:
            item = item.replace(word,' ')
        if len(item.strip()) == 0:
            count += 1

    return count