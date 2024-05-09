def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        filter_tree = ""
        for t in tree:
            if t in skill:
                filter_tree += t
        
        if filter_tree in skill:
            if skill.find(filter_tree) == 0:
                answer += 1
    
    return answer