from itertools import combinations

def solution(clothes):
    answer = 1
    clothes_map = dict()
    for clothe in clothes:
        kind = clothe[1]
        if kind not in clothes_map:
            clothes_map[kind] = list()
        clothes_map[kind].append(clothe[0])
            
    for kind in clothes_map.keys():
        answer *= len(clothes_map[kind]) + 1
    
    return answer - 1