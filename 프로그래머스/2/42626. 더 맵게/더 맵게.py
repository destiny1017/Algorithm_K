import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while True:
        val = heapq.heappop(scoville)
        if val >= K:
            break
        else:
            if len(scoville) > 0:
                sum = val + (heapq.heappop(scoville) * 2)
                heapq.heappush(scoville, sum)
                cnt += 1
            else:
                return -1
        
    return cnt