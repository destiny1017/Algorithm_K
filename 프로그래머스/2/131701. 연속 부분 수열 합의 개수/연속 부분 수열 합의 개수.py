from itertools import accumulate

def solution(elements):
    answer = 0
    accum_arr = list(accumulate(elements))
    total = set(elements)
    total.add(sum(elements))

    for i in range(1, len(elements)):
        st, ed = 0 - i, 0
        prev = st-1
        num = accum_arr[-1] - accum_arr[prev]
        
        for j in range(len(elements)):
            num -= elements[st]
            num += elements[ed]
            total.add(num)
            st += 1
            ed += 1
    return len(total)