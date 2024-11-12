import sys
input = sys.stdin.readline

n = int(input())
point_map = [(int(num), int(num)) for num in input().split()]

for i in range(n-1):
    arr = [int(num) for num in input().split()]
    new_map = []
    for j in range(len(arr)):
        if j == 0:
            min_val = min(point_map[j][0], point_map[j + 1][0]) + arr[j]
            max_val = max(point_map[j][1], point_map[j + 1][1]) + arr[j]
            new_map.append((min_val, max_val))
        elif j == 2:
            min_val = min(point_map[j][0], point_map[j - 1][0]) + arr[j]
            max_val = max(point_map[j][1], point_map[j - 1][1]) + arr[j]
            new_map.append((min_val, max_val))
        else:
            min_val = min(point_map[j][0], point_map[j - 1][0], point_map[j + 1][0]) + arr[j]
            max_val = max(point_map[j][1], point_map[j - 1][1], point_map[j + 1][1]) + arr[j]
            new_map.append((min_val, max_val))
    point_map = new_map

min_val, max_val = 1e9, 0
for val in point_map:
    min_val = min(min_val, val[0])
    max_val = max(max_val, val[1])

print(max_val, min_val)
