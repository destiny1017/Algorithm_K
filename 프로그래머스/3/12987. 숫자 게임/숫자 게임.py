def solution(A, B):
    lose = 0
    A.sort()
    B.sort()
    
    for i in range(len(B)):
        if B[i] <= A[i - lose]:
            lose += 1
    
    return len(A) - lose