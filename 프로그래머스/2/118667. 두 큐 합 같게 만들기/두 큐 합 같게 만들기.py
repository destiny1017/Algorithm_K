from collections import deque

def solution(queue1, queue2):
    answer = -1
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    dq1sum = sum(dq1)
    dq2sum = sum(dq2)
    
    for i in range(len(queue1)*3):
        if dq1sum < dq2sum:
            val = dq2.popleft()
            dq1.append(val)
            dq1sum += val
            dq2sum -= val
        elif dq1sum > dq2sum:
            val = dq1.popleft()
            dq2.append(val)
            dq1sum -= val
            dq2sum += val
        else:
            return i
    return answer