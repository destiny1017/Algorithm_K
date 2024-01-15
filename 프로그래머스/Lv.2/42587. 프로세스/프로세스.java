import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<priorObject> queue = new LinkedList<>();

        for (int i = 0; i < priorities.length; i++) {
            queue.add(new priorObject(priorities[i], i));
        }
        int cnt = 0;
        while(!queue.isEmpty()) {
            int top = 0;
            for (priorObject prior : queue) {
                int val = prior.getValue();
                if(top < val) {
                    top = val;
                }
            }
            priorObject peek = queue.peek();
            if(peek.getValue() >= top) {
                priorObject poll = queue.poll();
                cnt++;
                if(poll.getIndex() == location) {
                   return cnt;
                }
            } else {
                queue.offer(queue.poll());
            }
        }
        return 0;

    }
    
    class priorObject {
        Integer value;
        int index;

        public priorObject(Integer value, int index) {
            this.value = value;
            this.index = index;
        }

        public Integer getValue() {
            return value;
        }

        public void setValue(Integer value) {
            this.value = value;
        }

        public int getIndex() {
            return index;
        }

        public void setIndex(int index) {
            this.index = index;
        }
    }
}