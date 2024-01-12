def solution(score):
    
    data = sorted([(sum(mean)/2) for mean in score], reverse=True)
    
    return [data.index(sum(i)/2) + 1 for i in score]