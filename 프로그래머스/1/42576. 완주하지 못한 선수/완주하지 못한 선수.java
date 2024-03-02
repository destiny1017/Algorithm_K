import java.util.Arrays;

class Solution {
    public String solution(String[] participant, String[] completion) {  
    	Arrays.sort(participant);
    	Arrays.sort(completion);
    	String answer = participant[completion.length];  
    	for(int i=0; i<completion.length; i++) {
    			if(!participant[i].equals(completion[i])) {
    				answer = participant[i];
                    break;
    			}
    	} 	
        return answer;
    }
}