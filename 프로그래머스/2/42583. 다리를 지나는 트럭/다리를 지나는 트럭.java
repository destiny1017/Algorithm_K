import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        // 다리, 트럭 큐 생성후 기본값 채우기
        Queue<Integer> trucks = new LinkedList<>(Arrays.stream(truck_weights)
                                                 .boxed()
                                                 .collect(Collectors.toList()));
        Queue<Integer> bridge = new LinkedList<>(Collections.nCopies(bridge_length, 0));
        
        int total_weight = 0;
        while(!trucks.isEmpty()) {
            // 다리무게에서 가장 앞쪽 무게 빼기
            total_weight -= bridge.poll();
            // 다리 무게 한도까지 트럭 무게 빼서 집어넣기, 한도 도달하면 0 집어넣기 반복
            if(trucks.peek() + total_weight <= weight) {
                total_weight += trucks.peek();
                bridge.add(trucks.poll());
            } else {
                bridge.add(0);
            }
            answer += 1;
        }
        answer += bridge_length; // 마지막 트럭진입 후 다리 길이만큼 이동시간 추가
        
        return answer;
    }
}