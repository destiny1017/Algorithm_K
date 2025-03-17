import sys
from itertools import accumulate

def calc_profit(n, arr):
    accum = list(accumulate(arr))
    dp = [0] * n
    for i in range(1, n):
        j = i
        while j > 0 and arr[j-1] < arr[i]:
            j -= 1
        sum = accum[i-1] - accum[j-1] if j > 0 else accum[i-1]
        dp[i] = dp[j-1] + (arr[i] * (i - j) - sum)

    return dp[-1]

input = sys.stdin.readline
num = int(input())

for i in range(num):
    n = int(input())
    arr = [int(v) for v in input().split()]
    print(calc_profit(n, arr))