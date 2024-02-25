from itertools import combinations_with_replacement

def calc_divisor(n):
    divisor = []
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            if i != n // i:
                divisor.append(n // i)
    return divisor

def calc(arr, brown):
    return (arr[0] * 2) + ((arr[1]-2) * 2) == brown

def solution(brown, yellow):
    answer = []
    value = brown + yellow
    divisor = calc_divisor(value)
    
    for n, m in combinations_with_replacement(divisor, 2):
        if n * m == value:
            answer = sorted([n, m], reverse=True)
            if calc(answer, brown):
                return answer
    
    return answer
