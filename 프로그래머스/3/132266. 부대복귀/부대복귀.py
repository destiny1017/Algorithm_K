from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    INF = 10**6
    graph = [[] for _ in range(n + 1)]
    visit = [False] * (n+1)
    result = [INF] * (n+1)
    
    for st, ed in roads:
        graph[st].append(ed)
        graph[ed].append(st)
    
    queue = deque()
    queue.append((destination, 0))
    result[destination] = 0
    
    while queue:
        node, cnt = queue.popleft()
        if visit[node]:
            continue
        cnt += 1
        for v in graph[node]:
            if result[v] > cnt:
                result[v] = cnt
            queue.append((v, cnt))
        visit[node] = True
    
    for val in sources:
        answer.append(-1 if result[val] == 10**6 else result[val])
    
    return answer