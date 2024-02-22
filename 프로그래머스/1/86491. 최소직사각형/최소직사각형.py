def solution(sizes):
    answer = 0
    sorted_arr = list()
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sorted_arr.append([sizes[i][1], sizes[i][0]])
        else:
            sorted_arr.append([sizes[i][0], sizes[i][1]])
    
    max_val = max([row[0] for row in sorted_arr])
    min_val = max([row[1] for row in sorted_arr])
    return max_val * min_val