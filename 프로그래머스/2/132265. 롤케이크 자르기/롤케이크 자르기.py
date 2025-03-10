def solution(topping):
    answer = 0
    map1 = dict()
    map2 = dict()
    for t in topping:
        if t not in map1:
            map1[t] = 0
        map1[t] += 1
    
    map1_len = len(map1)
    map2_len = 0
    for i in range(len(topping)):
        if topping[i] not in map2:
            map2[topping[i]] = 0
            map2_len += 1
        map2[topping[i]] += 1
        map1[topping[i]] -= 1
        if map1[topping[i]] == 0:
            map1_len -= 1
        
        if map1_len == map2_len:
            answer += 1
        
        if map1_len < map2_len:
            break
        
        
    return answer