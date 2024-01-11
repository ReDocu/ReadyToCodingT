def solution(board):
    find_mine = [(i,j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == 1]
    
    danger_list = list()
    danger_list_plus = list()
    for mine in find_mine:
        danger_list += [(mine[0] + (x - 1), mine[1] + (y - 1)) for x in range(0,3) for y in range(0,3) if (mine[0] + (x - 1)) >= 0 and (mine[1] + (y - 1)) >= 0 and (mine[0] + (x - 1)) < len(board) and (mine[1] + (y - 1)) < len(board)]


    return len(board)**2 - len(set(danger_list))