import heapq

def solution(jobs):
    jobs.sort()
    answer = 0
    i = 0
    time = 0
    
    heap = []
    
    while len(jobs) > i or heap:  
        while i < len(jobs) and jobs[i][0] <= time:
            heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
            i += 1
        
        if heap:
            process = heapq.heappop(heap)
            answer += process[0] + (time - process[1])
            time += process[0]
        else:
            time += 1
    
    return answer // len(jobs)