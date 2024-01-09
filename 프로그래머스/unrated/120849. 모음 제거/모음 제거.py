def solution(my_string):
    words = ['a','e','i','o','u']
    
    for word in words:
        my_string = my_string.replace(word,'')
    
    return my_string