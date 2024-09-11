
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = [(prices[0], 0)]
    prices[-1] = 0
    for i in range(1, len(prices)):
        if prices[i] < prices[i-1]:
            while stack and stack[-1][0] > prices[i]:
                index = stack.pop()[1]
                answer[index] = i - index
        stack.append((prices[i], i))
    
    return answer