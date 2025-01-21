import heapq

def min_dist(graph, start):
    INF = 10**6
    distance = [INF] * len(graph)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, node = heapq.heappop(queue)
        if dist > distance[node]:
            continue
        
        for dest in graph[node]:
            cost = dist + 1
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(queue, (cost, dest))
    return distance

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]
    for st, ed in roads:
        graph[st].append(ed)
        graph[ed].append(st)
    
    result = min_dist(graph, destination)
    
    for val in sources:
        answer.append(-1 if result[val] == 10**6 else result[val])
    
    return answer