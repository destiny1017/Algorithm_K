import java.util.*;

class Solution {
    public int solution(int[] order) {
        int i = 0;
        int conveyor = 0;
        Stack<Integer> stack = new Stack<>();
        
        while(i < order.length) {
            if(order[i] == conveyor) {
                conveyor++;
                i++;
            } else if(!stack.isEmpty() && order[i] == stack.peek()) {
                stack.pop();
                i++;
            } else {
                if(order[i] > conveyor) {
                    stack.push(conveyor);
                    conveyor++;
                } else {
                    break;
                }
            }
        }
        
        return i;
    }
}