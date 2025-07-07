def solution(arr):
    answer = 0
    
    while True:
        answer += 2
        flag = True
        for a in arr:
            if answer % a != 0:
                flag = False
                break
        if flag:
            return answer
        
    return answer