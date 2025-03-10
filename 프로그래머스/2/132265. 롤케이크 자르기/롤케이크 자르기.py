def solution(topping):
    answer = 0
    map1 = dict()
    map2 = dict()
    for t in topping:
        if t not in map1:
            map1[t] = 0
        map1[t] += 1
    
    for i in range(len(topping)):
        if topping[i] not in map2:
            map2[topping[i]] = 0

        map2[topping[i]] += 1
        map1[topping[i]] -= 1
        
        if map1[topping[i]] == 0:
            del map1[topping[i]]
        
        if len(map1) == len(map2):
            answer += 1
        
        if len(map1) < len(map2):
            break
        
        
    return answer