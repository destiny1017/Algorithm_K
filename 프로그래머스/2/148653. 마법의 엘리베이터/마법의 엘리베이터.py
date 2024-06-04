
def solution(storey):
    answer = 0
    value = 100000000
    
    while storey > 0:
        val = abs(storey - value)
        val2 = abs(storey - (value // 10))
        if val > val2:
            value //= 10
            continue
        if val >= storey:
            value //= 10
            continue
        
        storey = val
        answer += 1
        # print(f"storey={storey}, val={val}, value={value}, cnt={answer}")
    
    return answer