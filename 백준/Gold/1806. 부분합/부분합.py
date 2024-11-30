n, s = map(int, input().split())
arr = [int(num) for num in input().split()]

st, ed = 0, 0
sum = arr[0]
min_len = len(arr) + 1

while st < len(arr) and ed < len(arr):
    if sum < s:
        ed += 1
        if ed >= len(arr):
            break
        sum += arr[ed]
    else:
        min_len = min(min_len, ed - st + 1)
        sum -= arr[st]
        st += 1

print(min_len if min_len <= len(arr) else 0)