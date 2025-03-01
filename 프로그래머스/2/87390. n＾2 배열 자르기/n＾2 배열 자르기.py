def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        val = i // n
        idx = i - (val * n)
        # print(f"i={i}, val={val}, idx={idx}")
        if idx < val:
            answer.append(val+1)
        else:
            answer.append(idx+1)
        
    return answer