import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

def dfs(num, times, graph, node_times, total):

    if len(graph[num]) == 0:
        return total + times[num]
    else:
        if node_times[num] == -1:
            require_times = []
            for node in graph[num]:
                require_times.append(dfs(node, times, graph, node_times, total))
            node_times[num] = total + max(require_times) + times[num]

        return node_times[num]

while n > 0:
    n -= 1
    k, m = map(int, input().split())
    times = [0] + [int(v) for v in input().split()]
    graph = [[] for _ in range(k+1)]
    node_times = [-1 for _ in range(k+1)]

    for i in range(m):
        x, y = map(int, input().split())
        graph[y].append(x)

    w = int(input())
    result = dfs(w, times, graph, node_times, 0)
    print(result)

