def solution(quiz):
    answer = list()
    for item in quiz:
        value, op_result = item.split('=')
        
        num1,op,num2 = value.split()

        if op == '+':
            if int(num1) + int(num2) == int(op_result):
                answer.append('O')
            else:
                answer.append('X')
        elif op == '-':
            if int(num1) - int(num2) == int(op_result):
                answer.append('O')
            else:
                answer.append('X')

    return answer