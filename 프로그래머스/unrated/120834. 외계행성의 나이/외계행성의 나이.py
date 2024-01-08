def solution(age):
    
    answer = ''
    words = ['a','b','c','d','e','f','g','h','i','j']

    for i in str(age):
        answer += words[int(i)]
    
    return answer