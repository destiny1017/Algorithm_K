import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

def binary(start, end, max):

    if start > end:
        return max

    mid = (start + end) // 2

    expense = 0
    for i in arr:
        if i < mid:
            expense += i
        else:
            expense += mid

    if expense == m:
        return mid
    elif expense < m:
        if max < mid:
            max = mid
        return binary(mid + 1, end, max)
    elif expense > m:
        return binary(start, mid - 1, max)


print(binary(0, max(arr), 0))