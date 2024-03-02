def solution(participant, completion):
    answer = ''
    completion_map = dict()
    for name in completion:
        if name in completion_map:
            completion_map[name] = completion_map[name] + 1
        else:
            completion_map[name] = 1
    
    for name in participant:
        if name not in completion_map or completion_map[name] == 0:
            return name
        else:
            completion_map[name] = completion_map[name] - 1
            
    return answer