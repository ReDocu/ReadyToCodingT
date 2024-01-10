def solution(array, n):
    return min([array[index] for index in ([i for i, num in enumerate(array) if abs(num - n)== min([abs(num - n) for num in array])])])


