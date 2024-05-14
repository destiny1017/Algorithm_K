def solution(sequence, k):
    answer = []
    s = e = len(sequence) - 1
    s_idx = 0
    e_idx = e
    n = sequence[e]
    while s >= 0 <= e:
        if n == k:
            #print(f"n={n}, s={s}, e={e}")
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