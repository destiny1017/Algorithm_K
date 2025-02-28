import heapq

def solution(numbers):
    answer = [-1] * len(numbers)
    heap = []
    for i in range(len(numbers)):
        while heap and heap[0][0] < numbers[i]:
            idx = heapq.heappop(heap)[1]
            answer[idx] = numbers[i]
        heapq.heappush(heap, (numbers[i], i))
    
    return answer