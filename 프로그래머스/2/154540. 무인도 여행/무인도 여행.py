from collections import deque


def bfs(board, x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    n = len(board)
    m = len(board[0])

    count = int(board[x][y])
    board[x][y] = 'X'
    queue = deque()

    queue.append((x, y))

    while queue:
        nx, ny = queue.pop()
        for i in range(4):
            kx = nx + dx[i]
            ky = ny + dy[i]
            if kx > n - 1 or kx < 0 or ky > m - 1 or ky < 0:
                continue
            if board[kx][ky] == 'X':
                continue
            count += int(board[kx][ky])
            board[kx][ky] = 'X'
            queue.append((kx, ky))

    return count


def solution(maps):
    answer = []
    board = []
    for i in maps:
        board.append(list(i))

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 'X':
                cnt = bfs(board, i, j)
                if cnt > 0:
                    answer.append(cnt)

    if len(answer) == 0:
        answer.append(-1)

    return sorted(answer)
