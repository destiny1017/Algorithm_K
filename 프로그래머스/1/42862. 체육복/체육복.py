def solution(n, lost, reserve):
    answer = 0
    duplicate_arr = []
    lost = sorted(lost)
    reserve = sorted(reserve)
    for num in reserve:
        if num in lost:
            duplicate_arr.append(num)
            lost.remove(num)
    
    for num in duplicate_arr:
        reserve.remove(num)

    del_arr = []
    for num in lost:
        l_num = num - 1
        r_num = num + 1
        if l_num in reserve:
            reserve.remove(l_num)
            del_arr.append(num)
        elif r_num in reserve:
            reserve.remove(r_num)
            del_arr.append(num)
    answer = n - (len(lost) - len(del_arr))
    return answer