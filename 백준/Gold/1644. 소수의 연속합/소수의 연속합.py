import math

def get_primes(n):
    is_primes = [False, False] + [True] * (n-1)
    primes = []

    for i in range(int(math.sqrt(n)) + 1):
        if is_primes[i]:
            for j in range(i*i, n+1, i):
                is_primes[j] = False

    for i in range(n+1):
        if is_primes[i]:
            primes.append(i)

    return primes

n = int(input())

primes = get_primes(n)
result = 0

st, ed = 0, 0
sum = primes[0] if primes else 0

while True:

    if st >= len(primes) or ed >= len(primes):
        break

    if sum == n:
        result += 1
        sum -= primes[st]
        st += 1
    elif sum < n:
        ed += 1
        if ed == len(primes):
            break
        sum += primes[ed]
    elif sum > n:
        sum -= primes[st]
        st += 1

print(result)