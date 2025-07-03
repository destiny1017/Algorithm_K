import bisect

def solution(operations):
    sorted_list = []
    left = 0
    for o in operations:
        command, value = o.split()
        int_val = int(value)
        if command == 'I':
            bisect.insort(sorted_list, int_val)
        else:
            if int_val == 1 and len(sorted_list) > left:
                sorted_list.pop()
            elif len(sorted_list) > left:
                sorted_list[left] = -10000000
                left += 1

    if left >= len(sorted_list):
        return [0, 0]

    return [sorted_list[-1], sorted_list[left]]