def solution(citations):
    answer = 0
    citations.sort()
    pivot = 0
    for i in range(len(citations)):
        h = len(citations) - i
        if citations[i] >= h:
            answer = h
            break
    
    return answer