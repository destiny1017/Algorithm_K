# https://www.acmicpc.net/problem/1922
import sys

v = int(sys.stdin.readline())
n = int(sys.stdin.readline())

parent = [i for i in range(v+1)]
edges = []

def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]

def union_parent(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

for i in range(n):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))

edges.sort()
total_cost = 0

for i in range(n):
    cost, a, b = edges[i]
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    union_parent(parent, a, b)
    total_cost += cost

print(total_cost)