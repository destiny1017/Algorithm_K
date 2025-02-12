def solution(n, stations, w):
    answer = 0
    parts = []
    i = 0
    st, ed = 0, 0
    flag = False
    while i < len(stations):
        st = stations[i] - w
        ed = stations[i] + w
        
        while i < len(stations) and stations[i] - w <= ed + 1:
            ed = stations[i] + w
            i += 1
        
        parts.append((st, ed))

    if parts[-1][1] < n:
        parts.append((n+1, n))
    # print(parts)
    prev = 0
    cover_length = w * 2 + 1
    for i in range(len(parts)):
        fill_length = parts[i][0] - prev - 1
        answer += fill_length // cover_length
        if fill_length % cover_length != 0:
            answer += 1
        # print(answer)
        prev = parts[i][1]
    
    return answer