import sys
import math

n = int(sys.stdin.readline())
stars = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]
parent = [i for i in range(n)]
costs = []
total_cost = 0

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        x = abs(stars[j][0] - stars[i][0]) ** 2
        y = abs(stars[j][1] - stars[i][1]) ** 2
        costs.append([math.sqrt(x + y), i, j])

costs.sort()

def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, parent[x])
    return p[x]

def union_parent(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)

    if a < b:
        p[b] = a
    else:
        p[a] = b

for cost, a, b in costs:
    if find_parent(parent, a) == find_parent(parent, b):
        continue

    union_parent(parent, a, b)
    total_cost += cost

print(f"{total_cost:.2f}")