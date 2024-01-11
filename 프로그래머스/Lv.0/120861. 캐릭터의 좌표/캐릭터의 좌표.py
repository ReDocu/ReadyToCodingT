def solution(keyinput, board):
    
    move = [0,0]
    for command in keyinput:
        if command == 'left':
            move[0] -= 1 if (move[0] - 1) >= -(board[0] // 2) else 0
        if command == 'right':
            move[0] += 1 if (move[0] + 1) <= (board[0] // 2) else 0
        if command == 'up':
            move[1] += 1 if (move[1] + 1) <= (board[1] // 2) else 0
        if command == 'down':
            move[1] -= 1 if (move[1] - 1) >= -(board[1] // 2) else 0
        
    return move