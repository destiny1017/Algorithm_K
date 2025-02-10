def solution(gems):
    answer = [0, len(gems)]
    gem_kinds = len(set(gems))
    gem_map = {gems[0]: 1}
    st, ed = 0, 0
    while ed < len(gems) and st <= ed:
        # print(st, ed, gem_map)
        if len(gem_map) < gem_kinds:
            ed += 1
            if ed == len(gems):
                break
            if gems[ed] not in gem_map:
                gem_map[gems[ed]] = 0
            gem_map[gems[ed]] += 1
        else:
            if answer[1] - answer[0] > ed - st:
                # print(st, ed)
                answer[0], answer[1] = st, ed
                
            gem_map[gems[st]] -= 1
            if gem_map[gems[st]] <= 0:
                del gem_map[gems[st]]
            st += 1
            
    answer[0] += 1
    answer[1] += 1
    return answer