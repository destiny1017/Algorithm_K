def solution(n, times):
    answer = binary_search(1, max(times)*n, n, times, max(times)*n)
    return answer

def binary_search(left, right, n, times, min_val):

    if left > right:
        return min_val

    mid = (left + right) // 2

    total = 0
    for time in times:
        total += mid // time

        if total > n:
            break

    if total >= n:
        min_val = mid
        return binary_search(left, mid - 1, n, times, min_val)
    else:
        return binary_search(mid + 1, right, n, times, min_val)