from functools import reduce
import math

def solution(arrayA, arrayB):
    answer = [0]
    
    # 각각 배열의 최대공약수 구하기
    gcd_a = reduce(math.gcd, arrayA)
    gcd_b = reduce(math.gcd, arrayB)
    nodivision_a, nodivision_b = True, True
    
    # 서로의 최대공약수로 하나라도 나누어떨어지면 False
    for num in arrayA:
        if num % gcd_b == 0:
            nodivision_a = False
            break
    
    for num in arrayB:
        if num % gcd_a == 0:
            nodivision_b = False
            break
    
    # 하나도 나누어떨어지지 않는 최대공약수 리스트에 추가
    if nodivision_a:
        answer.append(gcd_b)
    
    if nodivision_b:
        answer.append(gcd_a)
    
    # 최대값 리턴
    return max(answer)
