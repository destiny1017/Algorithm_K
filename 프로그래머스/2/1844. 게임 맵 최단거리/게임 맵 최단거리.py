from collections import deque

def bfs(maps):
    dx, dy = [0,0,-1,1], [1,-1,0,0]
    visit = [[False for _ in range(len(maps[0]))] 
             for _ in range(len(maps))]
    
    queue = deque([(0,0,1)])
    visit[0][0] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        # print(x,y,cnt)
        if x == len(maps)-1 and y == len(maps[0])-1:
            return cnt
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0 or visit[nx][ny] == True:
                continue
            
            # print(nx, ny, cnt)
            queue.append((nx, ny, cnt+1))
            visit[nx][ny] = True
    
    return -1

def solution(maps):
    return bfs(maps)