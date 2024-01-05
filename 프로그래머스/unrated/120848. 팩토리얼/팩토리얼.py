def solution(n):
    answer = n
    tmp = n
    for i in range(1, n+1):
        tmp = tmp / i
        if tmp >= 1:
            answer = i
        else:
            break
    return answer