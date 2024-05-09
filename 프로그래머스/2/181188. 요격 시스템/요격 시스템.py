def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    
    prev_ed = 0
    for st, ed in targets:
        if st >= prev_ed:
            prev_ed = ed
            answer += 1
    return answer