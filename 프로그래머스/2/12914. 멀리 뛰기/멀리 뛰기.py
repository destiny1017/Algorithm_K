def solution(n):
    dp = [1,2]
    for i in range(1, n-1):
        dp.append(dp[i-1] + dp[i])
    return 1 if n == 1 else dp[-1] % 1234567