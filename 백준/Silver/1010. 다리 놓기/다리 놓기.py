# 테스트 케이스 개수 입력
t = int(input())

for _ in range(t):
    # 다리를 놓을 서쪽과 동쪽의 사이트 개수 입력
    n, m = map(int, input().split())

    # 다리를 놓을 수 있는 경우의 수를 저장할 dp 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 초기 조건 설정
    for i in range(m + 1):
        dp[1][i] = i

    # DP로 경우의 수 계산
    for i in range(2, n + 1):
        for j in range(i, m + 1):
            for k in range(j, i - 1, -1):
                dp[i][j] += dp[i - 1][k - 1]

    # 다리를 놓을 수 있는 경우의 수 출력
    print(dp[n][m])