import sys

n = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
result = "-1"

# 역방향 순회
for i in range(len(target)-1, 0, -1):
    # 좌측 요소가 현재 요소보다 더 작으면 좌측 요소를 pivot으로 선정
    if target[i-1] < target[i]:
        # pivot 우측 요소들 중 pivot보다 큰 가장 작은값을 찾아 swap
        min = i
        for j in range(i+1, len(target)):
            if target[min] > target[j] > target[i-1]:
                min = j
        target[i-1], target[min] = target[min], target[i-1]
        # pivot 우측의 값들을 오름차순 정렬
        target[i:] = sorted(target[i:])
        result = " ".join(str(x) for x in target)
        break

print(result)