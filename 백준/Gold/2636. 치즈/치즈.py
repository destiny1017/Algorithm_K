from collections import deque

n, m = map(int, input().split())
board = [[] for _ in range(n)]
for i in range(n):
    board[i] = input().split()

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

def bfs(tx, ty):
    queue = deque()
    board[tx][ty] = '2'
    queue.append((tx, ty))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == '0':
                board[nx][ny] = '2'
                queue.append((nx, ny))

def change_air():
    for i in range(n):
        for j in range(m):
            if (i == 0 or i == n - 1) and board[i][j] == '0':
                bfs(i, j)
            else:
                if board[i][0] == '0':
                    bfs(i, 0)
                if board[i][m-1] == '0':
                    bfs(i, m-1)
                break

def change_cheese():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == '1':
                cnt += 1
                for k in range(4):
                    kx, ky = i + dx[k], j + dy[k]
                    if kx < 0 or kx >= n or ky < 0 or ky >= m:
                        continue
                    if board[kx][ky] == '2':
                        board[i][j] = '3'
                        break
    return cnt

def change_cheese_air():
    for i in range(n):
        for j in range(m):
            if board[i][j] == '3':
                board[i][j] = '2'
                for k in range(4):
                    kx, ky = i + dx[k], j + dy[k]
                    if kx < 0 or kx >= n or ky < 0 or ky >= m:
                        continue
                    if board[kx][ky] == '0':
                        bfs(kx, ky)

change_air()

cycle_cnt = 0
last_cheese_cnt = 0
while True:
    cheese_cnt = change_cheese()
    if cheese_cnt:
        cycle_cnt += 1
        last_cheese_cnt = cheese_cnt
        change_cheese_air()
    else:
        print(cycle_cnt)
        print(last_cheese_cnt)
        break

