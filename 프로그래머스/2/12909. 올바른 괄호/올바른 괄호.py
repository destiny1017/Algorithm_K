from collections import deque

def solution(s):
    answer = True
    dq = deque()
    for char in s:
        if char == '(':
            dq.append(char)
        else:
            if len(dq) > 0:
                dq.pop()
            else:
                return False
    
    if len(dq) > 0:
        return False
    
    return True