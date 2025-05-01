
def solution(points, routes):
    answer = 0
    points = [[0, 0]] + points
    robots_move = [[] for _ in range(len(routes))]

    for i in range(len(routes)):
        robots_move[i].append(points[routes[i][0]])
        j = 1
        while j < len(routes[i]):
            now_move = robots_move[i][-1].copy()
            target_move = points[routes[i][j]]
            # 목적지 도착했으면 다음 목적지로 변경
            if target_move == now_move:
                j += 1
                if j < len(routes[i]):
                    target_move = points[routes[i][j]]
                else:
                    break

            # r,c 중 r부터 맞추기
            if now_move[0] != target_move[0]:
                now_move[0] += 1 if now_move[0] < target_move[0] else -1
            else:
                now_move[1] += 1 if now_move[1] < target_move[1] else -1
            robots_move[i].append(now_move)

    # for move in robots_move:
    #     print(move)

    step = 0
    while True:
        move_set = set()
        collision_set = set()
        for robot in robots_move:
            if len(robot) > step:
                move = tuple(robot[step])
                if move in move_set:
                    collision_set.add(move)
                else:
                    move_set.add(move)
        if len(move_set) == 0 and len(collision_set) == 0:
            break
        answer += len(collision_set)
        step += 1

    return answer
