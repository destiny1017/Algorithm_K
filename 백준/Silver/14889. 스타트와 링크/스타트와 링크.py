from itertools import combinations, permutations
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
items = [i+1 for i in range(n)]

cases = list(combinations(items, n // 2))
diff = 2**31

for i in range(len(cases)//2):
    a = cases[i]
    b = cases[len(cases) - 1 - i]
    # print(a, b)
    a_case = list(permutations(a, 2))
    b_case = list(permutations(b, 2))
    # print(a_case)
    # print(b_case)
    point_a = 0
    point_b = 0
    for j in range(len(a_case)):
        # print(arr[a_case[j][0]-1][a_case[j][1]-1])
        point_a += arr[a_case[j][0]-1][a_case[j][1]-1]
        point_b += arr[b_case[j][0]-1][b_case[j][1]-1]

    diff = min(diff, abs(point_a - point_b))

    # x, y = cases[i]

print(diff)