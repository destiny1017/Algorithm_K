from collections import deque

def solution(x, y, n):
    answer = 10**6
    queue = deque([(0, x)])
    sets = set()
    
    while queue:
        idx, val = queue.popleft()
        if val in sets:
            continue
        sets.add(val)
        
        if val == y:
            answer = min(answer, idx)
        elif val < y:
            queue.append((idx+1, val*3))
            queue.append((idx+1, val*2))
            queue.append((idx+1, val+n))
    
    if answer == 10**6:
        return -1
    return answer