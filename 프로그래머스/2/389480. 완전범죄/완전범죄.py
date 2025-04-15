def solution(info, n, m):
    dp = [[1000 for _ in range(m)] for _ in range(len(info)+1)]
    dp[0][0] = 0
    for i in range(1, len(info)+1):
        a = info[i-1][0]
        b = info[i-1][1]
        for j in range(m):
            # case A
            dp[i][j] = min(dp[i][j], dp[i-1][j] + a)

            # case B
            if j + b < m:
                dp[i][j+b] = min(dp[i][j + b], dp[i-1][j])
    
    result = min(dp[len(info)])
    return -1 if result >= n else result