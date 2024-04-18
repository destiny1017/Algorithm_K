import sys
n, k = map(int, sys.stdin.readline().split())
arr = [int(i) for i in sys.stdin.readline().split()]

ed = sum = cnt = 0

for st in range(n):
    while sum < k and ed < n:
        sum += arr[ed]
        ed += 1

    if sum == k:
        cnt += 1
    sum -= arr[st]

print(cnt)
