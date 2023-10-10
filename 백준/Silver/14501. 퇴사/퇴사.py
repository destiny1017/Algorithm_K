# https://www.acmicpc.net/problem/14501
n = int(input())
dp, t, p = [0] * n, [0] * n, [0] * n

for i in range(len(dp)):
    t[i], p[i] = map(int, input().split())

for i in range(n):
    if i > 0:
        dp[i] = dp[i-1]

    for j in range(i, i-5, -1):
        if j < 0:
            break
        if t[j] + j == i + 1:
            if j > 0:
                dp[i] = max(dp[i], dp[j-1] + p[j])
            else:
                dp[i] = max(dp[i], p[j])

print(max(dp))

