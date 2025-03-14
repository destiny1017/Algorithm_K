import sys
h, w, x, y = map(int, sys.stdin.readline().split())
b = [[int(v) for v in sys.stdin.readline().split()] for _ in range(h+x)]
a = []

for i in range(h):
    a.append(b[i][:w])

for i in range(x, h):
    for j in range(y, w):
        a[i][j] = b[i][j] - b[i-x][j-y]
        b[i][j] = b[i][j] - b[i - x][j - y]

for i in range(h):
    for j in range(w):
        print(a[i][j], end=" ")
    print()
