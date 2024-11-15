import sys
import heapq
input = sys.stdin.readline
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    node1, node2, cost = map(int, input().split())
    graph[node1].append((node2, cost))
    graph[node2].append((node1, cost))

s, t = map(int, input().split())
min_cost = [1e9 for _ in range(v+1)]
min_cost[s] = 0
queue = []
heapq.heappush(queue, (0, s))

while queue:
    cost, node = heapq.heappop(queue)
    if min_cost[node] < cost:
        continue

    for toNode, toCost in graph[node]:
        total_cost = cost + toCost
        if min_cost[toNode] > total_cost:
            min_cost[toNode] = total_cost
            heapq.heappush(queue, (total_cost, toNode))

print(min_cost[t])