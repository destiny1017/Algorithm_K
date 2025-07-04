def solution(n, s):
    if n > s:
        return [-1]
    m, k = s // n, s % n
    return [m] * (n-k) + ([m+1] * k)
    