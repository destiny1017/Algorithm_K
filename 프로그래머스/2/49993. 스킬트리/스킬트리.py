def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        prev_idx = 0
        miss = False
        able = True
        for s in skill:
            idx = tree.find(s)
            if miss and idx >= 0:
                able = False
                break
            if idx == -1:
                miss = True
            elif idx < prev_idx:
                able = False
                break
            else:
                prev_idx = idx
        if able:
            answer += 1
    
    return answer