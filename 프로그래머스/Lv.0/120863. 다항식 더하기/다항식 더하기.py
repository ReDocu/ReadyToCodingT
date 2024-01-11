def solution(polynomial):
    temp_msg = polynomial.split('+')

    x_count = 0
    sub_count = 0
    for item in temp_msg:
        if item.find('x') != -1:
            if item.replace('x','').strip() == '':
                item = 1
            else:
                item = int(item.replace('x',''))
            x_count += item
        else:
            sub_count += int(item)

    if x_count == 0:
        return f'{sub_count}'
    elif sub_count == 0:
        return 'x' if x_count == 1 else f'{x_count}x'
    else:
        return f'x + {sub_count}' if x_count == 1 else f'{x_count}x + {sub_count}'