import sys
import heapq

INF = int(1e9)
v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
distance = [INF for _ in range(v+1)]
distance[start] = 0

for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

queue = []
heapq.heappush(queue, (0, start))

while queue:
    dist, node = heapq.heappop(queue)
    if distance[node] < dist:
        continue

    for toNode, toDist in graph[node]:

        if dist+toDist < distance[toNode]:
            distance[toNode] = dist+toDist
            heapq.heappush(queue, (dist+toDist, toNode))

for d in distance[1:]:
    if d == INF:
        print("INF")
    else:
        print(d)