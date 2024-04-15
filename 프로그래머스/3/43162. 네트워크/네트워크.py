def dfs(node, computers, visit):
    visit[node] = True
    for i in range(len(computers[node])):
        if not visit[i] and computers[node][i] == 1:
            dfs(i, computers, visit)

def solution(n, computers):
    visit = [False] * n
    cnt = 0
    for i in range(n):
        if not visit[i]:
            dfs(i, computers, visit)
            cnt += 1
    
    return cnt