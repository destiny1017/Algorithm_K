import java.util.*;

public class Solution {
	
	// 2019 KAKAO BLIND RECRUITMENT 오픈채팅방
	
	// 1. StringTokenizer를 통해 입력받은 레코드 구분
	// 2. ID, NAME 맵 생성 후 값 세팅
	// 3. record 배열 순회하며 result배열에 입/퇴장 여부에 따른 메시지 추가
	
    public static String[] solution(String[] record) {
    	String[] st;
    	HashMap<String, String> userInfo = new HashMap<>();
    	for (String value : record) {
			st = value.split(" ");
			String action = st[0];
			String id = st[1];
			String name = st.length > 2 ? st[2] : "";
			if("Enter".equals(action)) {
				userInfo.put(id, name);
			} else if("Change".equals(action)) {
				userInfo.put(id, name);
			}
			st = null;
		}
    	ArrayList<String> resultList = new ArrayList<>();
    	String[] answer;
    	for (int i = 0; i < record.length; i++) {
    		st = record[i].split(" ");
    		String action = st[0];
    		if(!"Change".equals(action)) {
    			String id = st[1];
    			String message = "";
    			if("Enter".equals(action)) {
    				message = userInfo.get(id) + "님이 들어왔습니다.";
    			} else if("Leave".equals(action)){
    				message = userInfo.get(id) + "님이 나갔습니다.";
    			}
    			resultList.add(message);
    		}
    		st = null;
		}
    	answer = resultList.toArray(new String[0]);
        return answer;
    }
}