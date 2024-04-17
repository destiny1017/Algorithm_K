# https://www.acmicpc.net/problem/3896

import math

n = int(input())
m = 1299709 + 1
prime = [True] * m

# 에라토스테네스의 체 만들기
for i in range(2, int(math.sqrt(m)) + 1):
    is_prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        val = i
        target = m - i
        while val < target:
            val += i
            prime[val] = False

# 수열 길이 판별
for i in range(n):
    x = int(input())
    if prime[x]:
        print(0)
        continue

    val1 = x - 1
    while not prime[val1]:
        val1 -= 1

    val2 = x + 1
    while not prime[val2]:
        val2 += 1

    print(val2 - val1)
