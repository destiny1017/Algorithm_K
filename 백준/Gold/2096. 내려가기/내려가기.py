import sys
input = sys.stdin.readline

n = int(input())
dp = [(int(num), int(num)) for num in input().split()]

for i in range(n-1):
    arr = [int(num) for num in input().split()]
    dp = [
        (min(dp[0][0], dp[1][0]) + arr[0], max(dp[0][1], dp[1][1]) + arr[0]),
        (min(dp[0][0], dp[1][0], dp[2][0]) + arr[1], max(dp[0][1], dp[1][1], dp[2][1]) + arr[1]),
        (min(dp[1][0], dp[2][0]) + arr[2], max(dp[1][1], dp[2][1]) + arr[2]),
    ]

min_val, max_val = 1e9, 0
for val in dp:
    min_val = min(min_val, val[0])
    max_val = max(max_val, val[1])

print(max_val, min_val)