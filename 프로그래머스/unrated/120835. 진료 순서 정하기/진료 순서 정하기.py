def solution(emergency):
    
    emergency_sort = sorted(emergency, reverse = True)
    
    return [emergency_sort.index(x) + 1 for x in emergency]