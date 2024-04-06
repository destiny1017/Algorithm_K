import math

def solution(n,a,b):
    answer = 1
    
    while True:
        # A와 B의 라운드 번호 계산
        ra = math.ceil(a / 2)
        rb = math.ceil(b / 2)
        
        # A와 B의 라운드 번호가 같으면 만난 것이므로 해당 라운드를 반환
        if ra == rb:
            return answer
        
        # 다음 라운드로 넘어가기
        a = ra
        b = rb
        answer += 1

    return answer