def solution(nums):
    max_cnt = len(nums) / 2  
    kinds = len(set(nums))
    
    if kinds > max_cnt:
        return max_cnt
    else:
        return kinds