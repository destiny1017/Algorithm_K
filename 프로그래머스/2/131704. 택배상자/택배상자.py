from collections import deque

def solution(order):
    conveyor = 1
    stack = []
    i = 0
    while i < len(order):
        if conveyor == order[i]:
            i += 1
            conveyor += 1
        elif stack and stack[-1] == order[i]:
            i += 1
            stack.pop()
        else:
            if order[i] > conveyor:
                stack.append(conveyor)
                conveyor += 1
            else:
                break
    
    return i