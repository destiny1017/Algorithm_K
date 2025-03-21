import sys
input = sys.stdin.readline
h, w = map(int, input().split())
arr = [int(v) for v in input().split()]
left, right = 0, w-1
max_left, max_right = 0, w-1
water = 0
total_water = 0

while left < right:
    if arr[left] < arr[right]:
        water += arr[max_left] - arr[left]
        left += 1
        if arr[left] > arr[max_left]:
            max_left = left
            total_water += water
            water = 0

    else:
        water += arr[max_right] - arr[right]
        right -= 1
        if arr[right] > arr[max_right]:
            max_right = right
            total_water += water
            water = 0

print(total_water + water)