from itertools import permutations

def solution(k, dungeons):
    answer = -1
    # k_map = {}
    # for key, value in dungeons:
    #     k_map[key] = value
    
    for perm in permutations(dungeons, len(dungeons)):
        cnt = 0
        remain_cost = k
        
        for min_k, cost in perm:
            if remain_cost >= min_k:
                remain_cost -= cost
                cnt += 1
            else:
                break
        
        answer = max(answer, cnt)
        
    return answer