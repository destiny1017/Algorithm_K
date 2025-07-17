from collections import defaultdict
import heapq

def solution(tickets):
    graph = defaultdict(list)

    # 우선순위 큐를 사용해서 도착지를 알파벳 순으로 정렬
    for start, end in tickets:
        heapq.heappush(graph[start], end)

    route = []

    def dfs(curr):
        while graph[curr]:
            next = heapq.heappop(graph[curr])
            dfs(next)
        route.append(curr)

    dfs("ICN")
    return route[::-1]  # 역순으로 경로 구성됨