import java.util.*;

class Solution {
    public String[] solution(String[][] plans) {
        List<String> answer = new ArrayList<>();
        Integer[][] time_plans = new Integer[plans.length][3];
        Map<Integer, String> homework_map = new HashMap<>();
        
        // 1. int 형식으로 리스트 변경
        for(int i = 0; i < plans.length; i++) {
            String[] time = plans[i][1].split(":");
            time_plans[i][0] = Integer.parseInt(time[0]) * 60 + Integer.parseInt(time[1]);
            time_plans[i][1] = plans[i][0].hashCode();
            time_plans[i][2] = Integer.parseInt(plans[i][2]);
            homework_map.put(plans[i][0].hashCode(), plans[i][0]);
        }

        // 2. 시작시간순으로 정렬
        Arrays.sort(time_plans, Comparator.comparing(a -> a[0]));

        // 3. 시간 1씩 증가시키며 작업 수행
        int time = 0;
        int plans_idx = 0;
        Stack<Integer[]> homework_stack = new Stack<>();
        while(!homework_stack.isEmpty() || plans_idx < plans.length) {
            time++;
            
            // 스택 끝에 과제 남은시간 감소시키고 0되면 완료처리
            if(!homework_stack.isEmpty()) {
                homework_stack.peek()[2] -= 1;
                if(homework_stack.peek()[2] <= 0) {
                    answer.add(homework_map.get(homework_stack.pop()[1]));
                }
            }

            // 현재 시간이 다음 과제 시작시간에 도달하면 스택에 추가
            if(plans_idx < plans.length) {
                if(time_plans[plans_idx][0] <= time) {
                    homework_stack.push(time_plans[plans_idx]);
                    plans_idx++;
                }
            }
        }

        return answer.toArray(new String[0]);
    }
}