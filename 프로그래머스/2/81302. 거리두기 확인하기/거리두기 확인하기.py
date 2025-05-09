def right_fail(n, m, place):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    for i in range(4):
        nx, ny = n + dx[i], m + dy[i]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        
        if place[nx][ny] == 'P':
            return True
        
        if place[nx][ny] == 'O':
            tx, ty = nx + dx[i], ny + dy[i]
            if tx < 0 or tx >= 5 or ty < 0 or ty >= 5:
                continue
            if place[tx][ty] == 'P':
                return True
    return False


def diagonal_fail(n, m, places):
    dx, dy = [-1, -1, 1, 1], [-1, 1, -1, 1]
    check = {
        0: [(-1, 0), (0, -1)],
        1: [(-1, 0), (0, 1)],
        2: [(0, -1), (1, 0)],
        3: [(0, 1), (1, 0)]
    }
    for i in range(4):
        nx, ny = n + dx[i], m + dy[i]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        if places[nx][ny] == 'P':
            if places[n + check[i][0][0]][m + check[i][0][1]] == 'O':
                return True
            if places[n + check[i][1][0]][m + check[i][1][1]] == 'O':
                return True
    return False


def check_place(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if right_fail(i, j, place) or diagonal_fail(i, j, place):
                    return 0
    return 1


def solution(places):
    answer = []

    for p in places:
        answer.append(check_place(p))

    return answer
