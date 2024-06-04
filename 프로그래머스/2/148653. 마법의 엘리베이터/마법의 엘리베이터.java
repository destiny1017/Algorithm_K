class Solution {
    public int solution(int storey) {
        int answer = 0;
        int value = 100000000;
        
        while(storey > 0) {
            int val = Math.abs(storey - value);
            if(val >= storey || val > Math.abs(storey - (value / 10))) {
                value /= 10;
                continue;
            }
            
            storey = val;
            answer++;
        }
        return answer;
    }
}