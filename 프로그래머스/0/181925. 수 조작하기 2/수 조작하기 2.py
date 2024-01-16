def solution(numLog):
    
    answer = ''
    dic = { 1 :'w', -1:'s',10:'d',-10:'a'}
    
    
    for key, value in enumerate(numLog):
        if key == len(numLog) - 1:
            break
            
        answer += dic[numLog[key + 1] - numLog[key]]
    
    return answer
            
        
        
        
        
    
    
    return answer