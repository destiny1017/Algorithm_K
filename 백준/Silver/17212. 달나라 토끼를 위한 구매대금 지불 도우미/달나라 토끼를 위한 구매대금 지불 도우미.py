n = int(input())
coins = [7,5,2,1]
dp = [n] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    for c in coins:
        if i >= c:
            dp[i] = min(dp[i-c] + 1, dp[i])

print(dp[-1])