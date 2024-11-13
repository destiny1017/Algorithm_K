import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // n과 m 입력 받기
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        scanner.nextLine(); // 개행 문자 소모

        // DNA 문자열 입력 받기
        String dna = scanner.nextLine();

        // A, C, G, T 각각의 최소 개수 입력 받기
        int A = scanner.nextInt();
        int C = scanner.nextInt();
        int G = scanner.nextInt();
        int T = scanner.nextInt();

        // 초기 A, C, G, T 개수 카운트 설정
        Map<Character, Integer> acgt = new HashMap<>();
        acgt.put('A', countChar(dna.substring(0, m - 1), 'A'));
        acgt.put('C', countChar(dna.substring(0, m - 1), 'C'));
        acgt.put('G', countChar(dna.substring(0, m - 1), 'G'));
        acgt.put('T', countChar(dna.substring(0, m - 1), 'T'));

        int result = 0;

        // 슬라이딩 윈도우로 DNA 서열 체크
        for (int i = 0; i <= n - m; i++) {
            // 새로운 문자 추가
            char newChar = dna.charAt(i + m - 1);
            acgt.put(newChar, acgt.get(newChar) + 1);

            // 조건 확인
            if (acgt.get('A') >= A && acgt.get('C') >= C && acgt.get('G') >= G && acgt.get('T') >= T) {
                result++;
            }

            // 이전 문자 제거
            char oldChar = dna.charAt(i);
            acgt.put(oldChar, acgt.get(oldChar) - 1);
        }

        System.out.println(result);
        scanner.close();
    }

    // 문자열에서 특정 문자의 개수를 세는 메서드
    private static int countChar(String str, char ch) {
        int count = 0;
        for (char c : str.toCharArray()) {
            if (c == ch) count++;
        }
        return count;
    }
}
