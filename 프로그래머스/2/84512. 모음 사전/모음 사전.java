import java.util.*;

class Solution {
    static List<String> result = new ArrayList<>();
    static char[] items = new char[]{'A', 'E', 'I', 'O', 'U'};

    public static void dfs(String word) {
        result.add(word);

        if(word.length() == 5) {
            return;
        }

        for(int i = 0; i < items.length; i++) {
            dfs(word + items[i]);
        }
    }

    public static int solution(String word) {
        int answer = 0;
        for(int i = 0; i < items.length; i++) {
            dfs(String.valueOf(items[i]));
        }
        for(int i = 0; i < result.size(); i++) {
            if(result.get(i).equals(word)) {
                return i+1;
            }
        }

        return 0;
    }
}