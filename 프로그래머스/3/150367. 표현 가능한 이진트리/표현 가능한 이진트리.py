from bisect import bisect_left

# 더이상 분할할 수 없을 때까지 좌우로 분할하며 부모값과 자신값 비교하여 결과 반환
def recursive(arr, parent):
    mid = len(arr) // 2
    disconnect = arr[mid] == '1' and parent == '0'
    
    if mid == 0:
        return disconnect
    
    return recursive(arr[:mid], arr[mid]) or recursive(arr[mid+1:], arr[mid]) or disconnect
    

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
        
        # 트리 구성 가능 여부 재귀호출
        disconnect = recursive(bin_num, bin_num[len(bin_num) // 2])
        answer.append(0 if disconnect else 1)
        
    return answer