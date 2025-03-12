from itertools import accumulate

def solution(elements):
    accum_arr = list(accumulate(elements))
    total = set()

    for i in range(len(elements)):
        num = accum_arr[-1] - accum_arr[-1 - i]
        for j in range(len(elements)):
            num -= elements[j-i]
            num += elements[j]
            total.add(num)

    return len(total)