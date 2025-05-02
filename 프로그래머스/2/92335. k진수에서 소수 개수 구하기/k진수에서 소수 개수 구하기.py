import math

def solution(n, k):
    answer = 0
    val = n
    result = ""
    while val >= k:
        result += str(val % k)
        val = val // k
    result += str(val)
    c = result[::-1]

    def isPrime(n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    prev = -1
    for i in range(len(c)):
        if c[i] == '0':
            if abs(i - prev) != 1 and isPrime(int(c[prev+1:i])):
                answer += 1
            prev = i

    if prev < len(c)-1:
        answer += isPrime(int(c[prev+1:]))

    return answer