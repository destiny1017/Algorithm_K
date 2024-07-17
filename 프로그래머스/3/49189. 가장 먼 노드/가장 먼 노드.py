import heapq

def solution(n, edge):
    graph = [[] for i in range(n+1)]
    distance = [20000 for i in range(n+1)]
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    queue = []
    heapq.heappush(queue, (0, 1))
    distance[1], distance[0] = 0, 0
    
    while queue:
        dist, node = heapq.heappop(queue)
        
        if distance[node] < dist:
            continue
        
        for i in graph[node]:
            if dist+1 < distance[i]:
                distance[i] = dist+1
                heapq.heappush(queue, (dist+1, i))
    
    return distance.count(max(distance))