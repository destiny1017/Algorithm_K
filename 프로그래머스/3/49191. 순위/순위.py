def solution(n, results):
    answer = 0
    graph = [[None for _ in range(n)] for _ in range(n)]

    for win, lose in results:
        graph[win-1][lose-1] = True
        graph[lose-1][win-1] = False

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] is None:
                    continue
                if graph[i][k] == graph[k][j]:
                    graph[i][j] = graph[i][k]


    for i in range(n):
        result = True
        for j in range(n):
            if i != j and graph[i][j] == None:
                result = False
                break
        if result:
            answer += 1

    return answer