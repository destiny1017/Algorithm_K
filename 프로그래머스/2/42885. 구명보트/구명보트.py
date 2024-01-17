
def solution(people, limit):
    answer = 0
    people.sort()
    min, max = 0, len(people) - 1
    while min < max:
        if people[min] + people[max] > limit:
            max -= 1
        else:
            min += 1
            max -= 1
        answer += 1
    
    if min == max:
        answer += 1
    
    return answer