
def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key= lambda num : num*3, reverse=True)
    answer = int(''.join(str_numbers))
    return str(answer)

