
def solution(scores):
    answer = 1
    sorted_score = sorted(scores, key=lambda x: (-x[0], x[1]))
    wan = scores[0]
    wan_score = wan[0] + wan[1]
    r = 0
    
    for score in sorted_score:
        if score[0] > wan[0] and score[1] > wan[1]:
            return -1
        
        if score[1] >= r:
            r = score[1]
            if score[0] + score[1] > wan_score:
                answer += 1
            
    return answer
