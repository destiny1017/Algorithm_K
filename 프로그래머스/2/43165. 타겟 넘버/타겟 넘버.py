from itertools import product

def solution(numbers, target):
    answer = 0
    numbers_symbol = []
    for number in numbers:
        numbers_symbol.append([number, -number])
    
    for result in product(*numbers_symbol):
        sum = 0
        for i in result:
            sum += i
            
        if sum == target:
            answer += 1
    
    return answer