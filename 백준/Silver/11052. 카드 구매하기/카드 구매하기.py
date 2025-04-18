n = int(input())
cards = [int(v) for v in input().split()]
dp = cards[:]

for i in range(n):
    for j in range(i):
        dp[i] = max(dp[i], dp[i-j-1] + dp[j])

print(dp[-1])

