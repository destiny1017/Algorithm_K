def floyd_warshall(n, edges):
    # 초기 거리 배열 생성: 무한대로 초기화
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]

    # 자기 자신까지의 거리는 0
    for i in range(n):
        dist[i][i] = 0

    # 주어진 간선 정보로 초기화 (무방향 그래프라면 양방향으로 설정)
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)  # 무방향일 경우 필요

    # 플로이드-워셜 알고리즘 핵심
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def solution(n, s, a, b, fares):
    answer = float('inf')
    dist = floyd_warshall(n+1, fares)
    for i in range(1, n+1):
        answer = min(answer, dist[i][s] + dist[i][a] + dist[i][b])
    
    return answer