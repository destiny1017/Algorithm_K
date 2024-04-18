# https://www.acmicpc.net/problem/11659
import sys
n, m = map(int, sys.stdin.readline().split())
arr = [int(i) for i in sys.stdin.readline().split()]
sum_arr = [0]

for i in range(n):
    sum_arr.append(sum_arr[i] + arr[i])

for i in range(m):
    st, ed = map(int, sys.stdin.readline().split())
    print(sum_arr[ed] - sum_arr[st-1])
