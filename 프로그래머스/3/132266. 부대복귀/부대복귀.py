from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]
    result = [-1] * (n+1)
    
    for st, ed in roads:
        graph[st].append(ed)
        graph[ed].append(st)
    
    queue = deque()
    queue.append((destination, 0))
    result[destination] = 0
    
    while queue:
        node, cnt = queue.popleft()
        cnt += 1
        for v in graph[node]:
            if result[v] == -1:
                result[v] = cnt
                queue.append((v, cnt))
    
    for val in sources:
        answer.append(result[val])
    
    return answer