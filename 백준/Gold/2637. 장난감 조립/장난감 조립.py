import sys

input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [{} for _ in range(n+1)]
costs = [{} for _ in range(n+1)]

for i in range(m):
    x, y, k = map(int, input().split())
    graph[x][y] = k

def dfs(num):
    now_cost = {}
    for node in graph[num].keys():
        if not graph[node]:
            now_cost.setdefault(node, 0)
            now_cost[node] += graph[num][node]
        else:
            if not costs[node]:
                costs[node] = dfs(node)

            for c in costs[node].keys():
                now_cost.setdefault(c, 0)
                now_cost[c] += costs[node][c] * graph[num][node]

    return now_cost

result = dfs(n)
for key in sorted(result.keys()):
    print(f"{key} {result[key]}")