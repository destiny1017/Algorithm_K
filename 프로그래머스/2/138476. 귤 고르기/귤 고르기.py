# from collections import deque

def solution(k, tangerine):
    count_map = dict()
    cnt = 0
    
    for v in tangerine:
        if v not in count_map:
            count_map[v] = 0
        count_map[v] += 1
    kinds = sorted(list(count_map.values()), reverse=True)
    
    for i in range(len(kinds)):
        cnt += kinds[i]
        if cnt >= k:
            return i+1
    
    return 1