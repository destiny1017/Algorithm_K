# https://www.acmicpc.net/problem/2252

from collections import deque

v, e = map(int, input().split())

graph = [[] for _ in range(v + 1)]
indegree = [0 for _ in range(v + 1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    indegree[b] += 1

queue = deque()
result = []

for i in range(1, len(indegree)):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    val = queue.popleft()
    result.append(val)

    for vertex in graph[val]:
        indegree[vertex] -= 1
        if indegree[vertex] == 0:
            queue.append(vertex)

print(" ".join(str(i) for i in result))

