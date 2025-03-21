n = int(input())
graph = [0] * (n+1)
result_set = set()

for i in range(1, n+1):
    graph[i] = int(input())

def dfs(visit, graph, dest):
    if dest in visit:
        visit[dest] = True
        return visit

    visit[dest] = True
    return dfs(visit, graph, graph[dest])

for i in range(1, n+1):
    visit = dict()
    visit[i] = False
    result = dfs(visit, graph, graph[i])

    if not list(result.values()).count(False):
        result_set.update(result.keys())


print(len(result_set))
for num in sorted(result_set):
    print(num)