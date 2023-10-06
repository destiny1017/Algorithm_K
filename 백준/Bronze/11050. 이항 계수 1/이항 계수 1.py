from itertools import combinations
n, k = map(int, input().split())
print(len(list(combinations([1] * n, k))))