from collections import deque
n, m = map(int, input().split())
values = [int(v) for v in input().split()]
q = deque([int(i) for i in range(1, n+1)])
move = 0

for i in range(m):
    idx = q.index(values[i])
    if idx <= len(q) - idx:
        while q[0] != values[i]:
            q.append(q.popleft())
        q.popleft()
        move += idx
    else:
        while q[0] != values[i]:
            q.appendleft(q.pop())
        move += len(q) - idx
        q.popleft()

print(move)