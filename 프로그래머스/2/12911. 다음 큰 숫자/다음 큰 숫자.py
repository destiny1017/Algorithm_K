def solution(n):
    answer = n+1
    n_binary = bin(n)[2:].count('1')
    while answer < 1000000:
        if bin(answer)[2:].count('1') == n_binary:
            return answer
        answer += 1
        
    return answer