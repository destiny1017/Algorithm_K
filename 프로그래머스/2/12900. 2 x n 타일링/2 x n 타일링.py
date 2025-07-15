
def solution(n):
    a, b = 1, 1
    
    for i in range(n-1):
        c = a + b
        a, b = b, c
    
    return b % 1000000007