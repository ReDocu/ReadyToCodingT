def solution(s):
    msg = ''
    for i in sorted([item for item in s if s.count(item) == 1]):
        msg += i

    return msg