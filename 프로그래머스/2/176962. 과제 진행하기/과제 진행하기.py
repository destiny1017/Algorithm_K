'''
1. list 순회하며 hh:mm -> int로 변환하여 0인덱스로 위치 변경
2. 변경된 list 0 index 기준으로 오름차순 정렬 ex = [720, "korean", 30]
3. time 0 부터 시작, 반복당 1씩 증가시키며 스택에 쌓고, 가장 위의 자료는 남은시간 1씩 감소
4. 남은시간 모두 감소되면 pop 하고 바로다음 자료 시간 감소
'''

def solution(plans):
    answer = []
    plans_time = []
    # 1. int 변환
    for i in range(len(plans)):
        start_time = list(map(int, plans[i][1].split(":")))
        plans_time.append([
            start_time[0] * 60 + start_time[1],
            plans[i][0],
            int(plans[i][2])
        ])
    
    # 2. 시작시간순 정렬
    plans_time.sort(reverse=True)
    
    # 3. 과제 시작
    time = 0
    homework_stack = []
    while plans_time or homework_stack:
        time += 1
        # 잔여시간 감소
        if homework_stack:
            homework_stack[-1][2] -= 1
            if homework_stack[-1][2] <= 0:
                answer.append(homework_stack.pop()[1])
        
        # 시작시간 도달한 과제 추가
        if plans_time:
            if plans_time[-1][0] <= time:
                homework_stack.append(plans_time.pop())

    
    return answer