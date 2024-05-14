def solution(sequence):
    n = len(sequence)
    pdp = [-100000] * n
    mdp = [-100000] * n
    for i in range(n):
        pdp[i] = max(sequence[i] + mdp[i-1], sequence[i])
        mdp[i] = max((sequence[i] * -1) + pdp[i-1], sequence[i] * -1)
    
    return max(max(pdp), max(mdp))