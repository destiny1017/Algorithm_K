import math

def solution(picks, minerals):
    answer = 0
    costs = [{'diamond': 1, 'iron': 1, 'stone':1},
             {'diamond': 5, 'iron': 1, 'stone':1},
             {'diamond': 25, 'iron': 5, 'stone':1}]
    chunk_costs = []
    total_picks = sum(picks) * 5
    
    # 가지고 있는 곡괭이 수만큼 앞부분 부터 차례대로 청크로 분류
    for i in range(0, len(minerals), 5):
        if i >= total_picks:
            break
        
        # 해당 청크를 각각의 곡괭이로 캤을 때의 피로도 계산하여 저장
        chunk = minerals[i:i+5]
        cost_chunk = [0, 0, 0]
        for c in chunk:
            cost_chunk[0] += costs[0][c]
            cost_chunk[1] += costs[1][c]
            cost_chunk[2] += costs[2][c]
        chunk_costs.append(cost_chunk)
    
    # 가장 등급이 낮은 청크 기준으로 정렬
    chunk_costs = sorted(chunk_costs, key=lambda x: (x[2]))

    # 청크 갯수만큼의 좋은 곡괭이만 남기기
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
    
    # 가장 등급이 낮은 곡괭이부터 소모해가며 청크 캐기
    for chunk in chunk_costs:        
        while min_picks[pick_idx] == 0:
            pick_idx -= 1
        
        answer += chunk[pick_idx]
        min_picks[pick_idx] -= 1
    
    return answer