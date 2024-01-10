def solution(my_string):
    
    message = ''
    
    for msg in my_string:
        if msg.isupper() == True:
            message += msg.lower()
        if msg.islower() == True:
            message += msg.upper()
    
    return message