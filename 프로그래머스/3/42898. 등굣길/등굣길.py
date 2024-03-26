def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for xm, xn in puddles:
        dp[xn-1][xm-1] = -1
        
    dp[0][0] = 1
    for i in range(0, n):
        for j in range(0, m):
            if dp[i][j] == -1:
                dp[i][j] = 0
            elif i == 0 and j == 0:
                dp[0][0] = 1
            elif i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[-1][-1] % 1000000007