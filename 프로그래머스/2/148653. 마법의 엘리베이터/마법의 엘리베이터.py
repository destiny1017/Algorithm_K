
def solution(storey):
    answer = 0
    value = 100000000
    
    while storey > 0:
        val = abs(storey - value) # 현재 값에서 value를 뺀 절대값 구하기

        # 절대값이 현재 값보다 더 커지거나, 한단계 아래 버튼으로 뺀 것보다 크면 버튼 차감
        if val >= storey or val > abs(storey - (value // 10)):
            value //= 10
            continue
        
        storey = val
        answer += 1
    
    return answer