n = int(input())
graph = [[int(num) for num in input().split()] for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print()