'''
- 정렬 문제
- 정렬기준 : max 재생 장르, max 재생, min 고유번호
- 정렬 값 : index

1. 장르별 재생횟수 합산
2. 배열 : [장르재생횟수, 재생횟수, 고유번호]
'''

def solution(genres, plays):
    answer = []
    gen_map = {}
    
    # 장르별 재생횟수 합산
    for i, g in enumerate(genres):
        gen_map[g] = gen_map.setdefault(g, 0) + plays[i]
    
    # [장르재생횟수, 재생횟수, 고유번호] 배열 생성
    arr = []
    for i in range(len(plays)):
        arr.append([gen_map[genres[i]], plays[i], i])
    
    # 기준별 정렬
    arr = sorted(arr, key=lambda x: (-x[0], -x[1], x[2]))
    
    # 각 장르별로 최대 2개씩 담기
    best_arr = [arr[0][2]]
    before, before_idx = arr[0], 1
    for i in range(1, len(arr)):
        if before[0] != arr[i][0]:
            best_arr.append(arr[i][2])
            before = arr[i]
            before_idx = 1
        elif before_idx == 1:
            best_arr.append(arr[i][2])
            before_idx += 1
            
    return best_arr