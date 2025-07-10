import heapq


def solution(n, works):
    for i in range(len(works)):
        works[i] *= -1

    heapq.heapify(works)
    print(works)
    while n > 0:
        head = -heapq.heappop(works)
        if head == 0:
            n = 0
            break

        val = head - -works[0]
        if val <= 0:
            val += 1
        val = min(val, n)
        head -= val
        n -= val
        heapq.heappush(works, -head)
    
    for i in range(len(works)):
        works[i] = works[i] ** 2
    return sum(works)