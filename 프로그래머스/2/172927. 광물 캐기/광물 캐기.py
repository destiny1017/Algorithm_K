import math

def solution(picks, minerals):
    answer = 0
    costs = [{'diamond': 1, 'iron': 1, 'stone':1},
             {'diamond': 5, 'iron': 1, 'stone':1},
             {'diamond': 25, 'iron': 5, 'stone':1}]
    chunk_costs = []
    total_picks = sum(picks) * 5
    for i in range(0, len(minerals), 5):
        if i >= total_picks:
            break
        chunk = minerals[i:i+5]
        cost_chunk = [0, 0, 0]
        for c in chunk:
            cost_chunk[0] += costs[0][c]
            cost_chunk[1] += costs[1][c]
            cost_chunk[2] += costs[2][c]
        chunk_costs.append(cost_chunk)
    
    # last_chunk = chunk_costs.pop()
    
    chunk_costs = sorted(chunk_costs, key=lambda x: (x[2]))
    print(chunk_costs)

    pick_idx = 0
    cnt = 0
    min_picks = [0, 0, 0]
    while cnt < len(chunk_costs):
        if picks[pick_idx]:
            picks[pick_idx] -= 1
            min_picks[pick_idx] += 1
            cnt += 1
        else:
            pick_idx += 1
    
    
    while chunk_costs:
        chunk = chunk_costs[0]
        
        while min_picks[pick_idx] == 0:
            pick_idx -= 1
        
        answer += chunk[pick_idx]
        min_picks[pick_idx] -= 1
        
        del chunk_costs[0]
    
    return answer