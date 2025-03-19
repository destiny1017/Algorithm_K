import sys

def calc_profit(n, arr):
    profit = 0
    high = -1
    for i in reversed(range(n)):
        if arr[i] < arr[high]:
            profit += arr[high] - arr[i]
        elif arr[i] > arr[high]:
            high = i
    return profit

input = sys.stdin.readline
num = int(input())

for i in range(num):
    n = int(input())
    arr = [int(v) for v in input().split()]
    print(calc_profit(n, arr))