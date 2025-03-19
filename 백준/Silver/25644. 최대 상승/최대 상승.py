import sys
input = sys.stdin.readline

n = int(input())
profit = 0
min_val = 10**9

for price in [int(v) for v in input().split()]:
    profit = max(price - min_val, profit)
    min_val = min(min_val, price)

print(profit)