from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    total_weight = 0
    while trucks:
        total_weight -= bridge.popleft()
        if total_weight + trucks[0] <= weight:
            total_weight += trucks[0]
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
        answer += 1
    answer += bridge_length
    
    return answer