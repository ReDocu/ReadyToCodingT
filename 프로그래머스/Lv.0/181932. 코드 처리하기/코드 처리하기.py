def solution(code):
    
    
    msg = ''
    mode = False
    for i,item in enumerate(list(code)):
        if item == '1' and mode == True:
            mode = False
            continue
        elif item == '1' and mode == False:
            mode = True
            continue
            
        if mode == False and i % 2 == 0:
            msg += item
        
        if mode == True and i % 2 == 1:
            msg += item
    
    if msg == '':
        return 'EMPTY'
    
    return msg