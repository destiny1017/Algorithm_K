def solution(routes):
    answer = 0
    for i in range(len(routes)):
        routes[i].sort()
    
    routes.sort(key=lambda x: x[1])

    prev_ed = -30001
    for st, ed in routes:
        if st > prev_ed:
            prev_ed = ed
            answer += 1
    return answer