from itertools import permutations

def isPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, int((n ** 0.5)) + 1, 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    prime = set()
    for i in range(1, len(numbers)+1):
        result = list(permutations(numbers, i))
        for item in result:
            n = int("".join(i for i in item))
            if isPrime(n):
                prime.add(n)
    return len(prime)