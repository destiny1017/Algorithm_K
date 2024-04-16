# https://www.acmicpc.net/problem/20040
import sys

v, n = map(int, sys.stdin.readline().split())

parent = [i for i in range(v)]
result = 0

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
    v1, v2 = map(int, sys.stdin.readline().split())
    pv1 = find_parent(parent, v1)
    pv2 = find_parent(parent, v2)
    if pv1 == pv2:
        result = i+1
        break

    union_parent(parent, v1, v2)

print(result)

