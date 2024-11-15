n, m = map(int, input().split())
visit = [[False for _ in range(m)] for _ in range(n)]
board = []
result = 1

for i in range(n):
    board.append(list(input()))

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def dfs(st, cnt, block):
    global result
    x, y = st
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] in block:
            continue

        block.add(board[nx][ny])
        dfs((nx, ny), cnt+1, block)
        block.remove(board[nx][ny])

    result = max(result, cnt)

dfs((0,0), 1, set([board[0][0]]))

print(result)