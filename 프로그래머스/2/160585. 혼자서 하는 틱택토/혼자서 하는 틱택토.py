def solution(board):
    o, x = 0, 0
    co, xo = False, False
    for i in range(3):
        wo, wx = 0, 0
        ho, hx = 0, 0
        for j in range(3):
            if board[i][j] == 'O':
                wo += 1
            elif board[i][j] == 'X':
                wx += 1
            if board[j][i] == 'O':
                ho += 1
            elif board[j][i] == 'X':
                hx += 1
            
        if wo == 3 or ho == 3:
            co = True
        if wx == 3 or hx == 3:
            xo = True
        o += wo
        x += wx
    
    x1, o1 = 0, 0
    x2, o2 = 0, 0
    for i in range(3):
        if board[i][i] == 'O':
            o1 += 1
        elif board[i][i] == 'X':
            x1 += 1  
        if board[i][2 - i] == 'O':
            o2 += 1
        elif board[i][2 - i] == 'X':
            x2 += 1
    
    if o1 == 3 or o2 == 3:
        co = True
    if x1 == 3 or x2 == 3:
        xo = True
    
    # print(xo, co, x, o)
    if (co and xo) or x > o or o - x > 1:
        return 0
    if co and o - x != 1:
        return 0
    if xo and o != x:
        return 0
    return 1