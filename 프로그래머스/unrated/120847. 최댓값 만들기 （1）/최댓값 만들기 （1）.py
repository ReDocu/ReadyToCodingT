def solution(numbers):
    
    numbers_max = 0
    for i in numbers:
        for j in numbers:
            if i == j: 
                if numbers_max < max(numbers_max,i):
                    numbers_max = i
                continue
                
            if numbers_max < max(numbers_max,i*j):   
                numbers_max = max(numbers_max,i*j)      
        
    return numbers_max