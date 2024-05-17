import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        HashMap<String, Integer> gen_map = new HashMap<>();
        for(int i = 0; i < plays.length; i++) {
            gen_map.put(genres[i], gen_map.getOrDefault(genres[i], 0) + plays[i]);
        }
        int[][] arr = new int[plays.length][3];
        
        for(int i = 0; i < plays.length; i++) {
            arr[i] = new int[] {gen_map.get(genres[i]), plays[i], i};
        }
        
        Arrays.sort(arr, (n1, n2) -> {
            if(n1[0] == n2[0]) {
                if(n1[1] == n2[1]) {
                    return Integer.compare(n1[2], n2[2]);
                }
                return Integer.compare(n2[1], n1[1]);
            } else {
                return Integer.compare(n2[0], n1[0]);
            }
        });
        
        ArrayList<Integer> best_arr = new ArrayList<>();
        
        best_arr.add(arr[0][2]);
        int[] before = arr[0];
        int before_cnt = 1;
        for(int i = 1; i < arr.length; i++) {
            if(before[0] != arr[i][0]) {
                best_arr.add(arr[i][2]);
                before = arr[i];
                before_cnt = 1;
            } else if(before_cnt == 1) {
                best_arr.add(arr[i][2]);
                before_cnt += 1;
            }
        }
        answer = new int[best_arr.size()];
        for(int i = 0; i < answer.length; i++) {
            answer[i] = best_arr.get(i);
        }
        return answer;
    }
}