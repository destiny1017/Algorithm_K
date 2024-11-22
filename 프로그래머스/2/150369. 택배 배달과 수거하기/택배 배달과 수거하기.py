def working(work_stack, cap):
    while work_stack:
        pop = work_stack.pop()
        if pop <= cap:
            cap -= pop
        else:
            pop -= cap
            work_stack.append(pop)
            return work_stack
    return work_stack

def solution(cap, n, deliveries, pickups):
    answer = 0
    working(deliveries, 0)
    working(pickups, 0)
    while deliveries or pickups:
        now_cap = cap
        answer += max(len(deliveries), len(pickups)) * 2
        deliveries = working(deliveries, now_cap)
        pickups = working(pickups, now_cap)

    return answer