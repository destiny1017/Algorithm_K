def plus_point(type_point, target, point):
    for point_map in type_point:
        indicators = tuple(point_map.keys())
        if target in indicators:
            point_map[target] += point
            break

def solution(survey, choices):
    answer = ""
    type_point = [
        {'T':0, 'R':0},
        {'C':0, 'F':0},
        {'M':0, 'J':0},
        {'A':0, 'N':0}
    ]
    
    for i in range(len(survey)):
        low_indi = survey[i][0]
        high_indi = survey[i][1]
        if choices[i] < 4:
            plus_point(type_point, low_indi, 4 - choices[i])
        elif choices[i] > 4:
            plus_point(type_point, high_indi, choices[i] - 4)
        
    
    for point_map in type_point:
        indicators = tuple(point_map.keys())
        if point_map[indicators[0]] < point_map[indicators[1]]:
            answer += indicators[1]
        elif point_map[indicators[1]] < point_map[indicators[0]]:
            answer += indicators[0]
        else:
            answer += min(indicators[0], indicators[1])
    
    return answer