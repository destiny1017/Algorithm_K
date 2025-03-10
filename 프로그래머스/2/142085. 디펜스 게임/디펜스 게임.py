import heapq

def solution(n, k, enemy):
    heap = []
    i = 0
    while i < len(enemy) and len(heap) < k:
        heapq.heappush(heap, enemy[i])
        i += 1
    
    for e in enemy[i:]:
        if heap[0] >= e:
            n -= e
        else:
            n -= heapq.heappop(heap)
            heapq.heappush(heap, e)
        
        if n < 0:
            break
        i += 1
    
    return i