def solution(N, number):
    answer = -1
    dp = [set() for _ in range(9)]
    dp[1].add(N)

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for val1 in dp[j]:
                for val2 in dp[i - j]:
                    dp[i].add(val1 + val2)
                    dp[i].add(val1 - val2)
                    dp[i].add(val1 * val2)
                    if val2 != 0:
                        dp[i].add(val1 // val2)

        if number in dp[i]:
            return i

    return answer