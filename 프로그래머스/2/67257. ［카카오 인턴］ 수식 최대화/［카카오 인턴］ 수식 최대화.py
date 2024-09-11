import re

def calc(exp, order):
    for i in range(3):
        result = []
        j = 0
        while j < len(exp):
            if exp[j] == order[i]:
                prev = int(result[-1])
                next = int(exp[j + 1])
                if order[i] == '*':
                    result[-1] = str(prev * next)
                elif order[i] == '+':
                    result[-1] = str(prev + next)
                elif order[i] == '-':
                    result[-1] = str(prev - next)
                j += 1
            else:
                result.append(exp[j])
            j += 1
        exp = result
    return abs(int(exp[0]))

def solution(expression):
    answer = 0
    arr = re.findall(r'\d+|[+\-*/]', expression)
    orders = ["*+-", "*-+", "+*-", "+-*", "-*+", "-+*"]
    for order in orders:
        answer = max(answer, calc(arr, order))

    return answer