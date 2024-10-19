import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF for _ in range(n)] for _ in range(n)]

# 자기자신 비용 0 으로 초기화
for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

# 최소 이동 비용 입력
for i in range(m):
    st, ed, cost = map(int, input().split())
    graph[st-1][ed-1] = min(graph[st-1][ed-1], cost)

# k노드를 거쳐가는 최소비용 업데이트
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 출력
for i in range(n):
    for j in range(n):
        print(0 if graph[i][j] == INF else graph[i][j], end=" ")
    print()
