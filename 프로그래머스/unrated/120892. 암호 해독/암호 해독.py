def solution(cipher, code):
    
    msg = ''
    for i in range(code - 1,len(cipher),code):
        msg += cipher[i]
    
    return msg