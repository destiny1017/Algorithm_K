from collections import deque

def solution(x, y, n):
    answer = 10**6
    queue = deque([(0, x)])
    sets = set()
    
    while queue:
        idx, val = queue.popleft()
        # print(idx, val)
        if val in sets:
            continue
        else:
            sets.add(val)
        
        if val == y:
            answer = min(answer, idx)
        else:
            if val * 3 <= y:
                queue.append((idx+1, val*3))
            if val * 2 <= y:
                queue.append((idx+1, val*2))
            if val + n <= y:
                queue.append((idx+1, val+n))
    
    if answer == 10**6:
        return -1
    return answer