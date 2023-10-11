n, k = map(int, input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
items = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(1, n+1):
    weight, value = items[i-1]
    for j in range(1, k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[n][k])