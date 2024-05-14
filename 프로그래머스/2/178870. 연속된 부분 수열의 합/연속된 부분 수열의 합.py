def solution(sequence, k):
    # 배열 끝에서 시작
    s = e = len(sequence) - 1 
    s_idx, e_idx = 0, e
    n = sequence[e]
    
    # 부분수열의 합이 k보다 작거나 같으면 s를, 크면 e를 줄이기 반복. 0이 될 때까지
    while s > -1 < e:
        if n == k: 
            # 부분수열 합이 k와 같고 기존 배열보다 길이가 짧다면 인덱스 교체
            if abs(s - e) <= abs(s_idx - e_idx):
                s_idx, e_idx = s, e
            s -= 1
            n += sequence[s]
        elif n < k:
            s -= 1
            n += sequence[s]
        elif n > k:
            n -= sequence[e]
            e -= 1
    
    return [s_idx, e_idx]