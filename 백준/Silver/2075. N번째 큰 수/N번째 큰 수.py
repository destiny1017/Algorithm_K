import sys
import heapq
input = sys.stdin.readline

n = int(input())
queue = []

for num in input().split():
    heapq.heappush(queue, int(num))

for i in range(n-1):
    for num in input().split():
        heapq.heappush(queue, int(num))
        heapq.heappop(queue)

print(heapq.heappop(queue))