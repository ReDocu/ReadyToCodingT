def solution(lines):    

    checkline = sorted(lines, key=lambda x:x[0])
    count = set()

    for x in range(checkline[0][0], checkline[0][1]):
        for y in range(checkline[1][0], checkline[1][1]):
            if x  == y:
                count.add(x)

    for x in range(checkline[1][0], checkline[1][1]):
        for y in range(checkline[2][0], checkline[2][1]):
            if x  == y:
                count.add(x)

    for x in range(checkline[2][0], checkline[2][1]):
        for y in range(checkline[0][0], checkline[0][1]):
            if x  == y:
                count.add(x)


    return len(count)