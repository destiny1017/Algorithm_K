from bisect import bisect_left

def recursive(arr, parent):
    mid = len(arr) // 2
    
    unperfect = arr[mid] == '1' and parent == '0'
    
    if mid != 0:
        child1 = recursive(arr[:mid], arr[mid])
        child2 = recursive(arr[mid+1:], arr[mid])
        # print(f"child1={child1}, child2={child2}")
        return child1 or child2 or unperfect
    
    return unperfect

def solution(numbers):
    answer = []
    mlen = [1, 3, 7, 15, 31, 63] # 포화이진트리 2진수 개수
    for num in numbers:
        # number 2진수 변환
        bin_num = bin(num)[2:] 
        
        # 포화이진트리 2진수 길이보다 적으면 앞을 0으로 채움
        perfect_len = mlen[bisect_left(mlen, len(bin_num))]
        diff = perfect_len - len(bin_num)
        if diff != 0:
            bin_num = ("0" * diff) + bin_num
        
        # 루트노드가 0인데 자식노드가 1이면 불가능
        # no_perfect = False
        # j = 0
        # for i in range(1, len(bin_num), 2):
        #     if len(bin_num) // 2
        #     if bin_num[i] == '0' and (bin_num[i-1] == '1' or bin_num[i+1] == '1'):
        #         no_perfect = True
        #         break
        # print(f"bin_num={bin_num}, bin_num[len(bin_num) // 2]={bin_num[len(bin_num) // 2]}")
        no_perfect = recursive(bin_num, bin_num[len(bin_num) // 2])
        
        answer.append(0 if no_perfect else 1)
        
    return answer