def solution(cap, n, deliveries, pickups):
    answer = 0
    d_idx = n - 1
    p_idx = n - 1

    # 뒤에서부터 처리할 위치를 찾아야 하므로 뒤에서부터 순회
    while d_idx >= 0 or p_idx >= 0:
        # 가장 먼 거리 계산
        while d_idx >= 0 and deliveries[d_idx] == 0:
            d_idx -= 1
        while p_idx >= 0 and pickups[p_idx] == 0:
            p_idx -= 1
        
        # 가장 먼 거리 기준 왕복 거리 추가
        farthest = max(d_idx, p_idx) + 1
        answer += farthest * 2

        # 남은 용량으로 처리
        now_cap = cap
        while d_idx >= 0 and now_cap > 0:
            if deliveries[d_idx] <= now_cap:
                now_cap -= deliveries[d_idx]
                deliveries[d_idx] = 0
                d_idx -= 1
            else:
                deliveries[d_idx] -= now_cap
                now_cap = 0
        
        now_cap = cap
        while p_idx >= 0 and now_cap > 0:
            if pickups[p_idx] <= now_cap:
                now_cap -= pickups[p_idx]
                pickups[p_idx] = 0
                p_idx -= 1
            else:
                pickups[p_idx] -= now_cap
                now_cap = 0

    return answer
