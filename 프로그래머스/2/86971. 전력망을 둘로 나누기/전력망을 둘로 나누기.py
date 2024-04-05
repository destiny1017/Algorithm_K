graph = []
visit = []
cnt = 0

def dfs(j):
    global graph, visit, cnt
    visit[j] = True
    cnt += 1
    for node in graph[j]:
        if not visit[node]:
            dfs(node)


def solution(n, wires):
    global graph, visit, cnt
    answer = 100
    graph = [[] for _ in range(n+1)]
    visit = [False for _ in range(n+1)]
    
    # 그래프 생성
    for node1, node2 in wires:
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    # 와이어에서 요소 하나씩 제거
    for i in range(len(wires)):
        n1, n2 = wires[i]
        graph[n1].remove(n2)
        graph[n2].remove(n1)
        
        tree_size = []
        
        for j in range(1, len(graph)):
            if not visit[j]:
                dfs(j)
                tree_size.append(cnt)
                cnt = 0
        
        answer = min(answer, abs(tree_size[0] - tree_size[1]))
        graph[n1].append(n2)
        graph[n2].append(n1)
        visit = [False for _ in range(n+1)]
    
    return answer