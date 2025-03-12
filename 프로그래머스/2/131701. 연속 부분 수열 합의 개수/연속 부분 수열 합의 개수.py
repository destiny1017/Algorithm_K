from itertools import accumulate

def solution(elements):
    elements.extend(elements)
    print(elements)
    return 1