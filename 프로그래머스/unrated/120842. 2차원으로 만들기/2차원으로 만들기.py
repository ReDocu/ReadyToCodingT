def solution(num_list, n):
    answer = list()
    for i in range(0, len(num_list)//n):
        answer.append([num_list[i * n + x] for x in range(0, n)])    
    return answer