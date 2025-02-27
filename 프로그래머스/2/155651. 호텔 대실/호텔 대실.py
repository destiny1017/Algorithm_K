import heapq

def solution(book_time):
    answer = 0
    heap = []
    book_time.sort(key=lambda x: x[0])
    for b in book_time:
        st = b[0].split(":")
        ed = b[1].split(":")
        st_time = int(st[0]) * 60 + int(st[1])
        ed_time = int(ed[0]) * 60 + int(ed[1]) + 10
        
        if heap and heap[0] <= st_time:
            heapq.heappop(heap)
        else:
            answer += 1
        
        heapq.heappush(heap, ed_time)

    return answer