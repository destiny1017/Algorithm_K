def solution(board):
    answer = 0
    
    start = ()
    goal = ()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start = [i, j, 0]
            elif board[i][j] == 'G':
                goal = (i, j)
    
    visit = [[False] * len(board[0]) for _ in range(len(board))]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    queue = [start]
    visit[start[0]][start[1]] = True
    
    # BFS 수행
    while queue:
        x, y, cnt = queue.pop()
        if board[x][y] == 'G':
            answer = cnt
            break
        
        # 4방향 탐색
        for i in range(4):
            nx, ny = x, y
            while True:
                nx += dx[i]
                ny += dy[i]
                
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]) or board[nx][ny] == 'D':
                    nx, ny = nx - dx[i], ny - dy[i] # 막혔으면 이전 좌표로 되돌리기
                    break
            
            # 방문하지 않은 좌표이면 횟수 1증가 후 큐에 추가
            if not visit[nx][ny] and (nx != x or ny != y):
                visit[nx][ny] = True
                queue.insert(0, [nx, ny, cnt+1])
            
    return answer if answer > 0 else -1