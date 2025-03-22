def solution(n):
    answer = [[0] * (i) for i in range(1, n+1)]
    step_move = [(1, 0), (0, 1), (-1, -1)]
    step, cnt = 0, 1
    i, j = -1, 0
    while n > 0:
        for k in range(n):
            i += step_move[step % 3][0]
            j += step_move[step % 3][1]
            answer[i][j] = cnt
            cnt += 1
        step += 1
        n -= 1
    return sum(answer, [])