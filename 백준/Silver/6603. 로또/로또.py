from itertools import combinations
import sys

while True:
    items = list(map(int, sys.stdin.readline().split()))
    if len(items) == 1:
        break

    for case in combinations(items[1:], 6):
        print(" ".join(str(i) for i in case))

    print()
