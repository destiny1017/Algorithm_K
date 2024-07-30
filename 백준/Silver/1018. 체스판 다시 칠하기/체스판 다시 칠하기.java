import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static char board[][];

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		board = new char[n][m];
		for (int i = 0; i < n; i++) {
			board[i] = br.readLine().toCharArray();
		}
		
		char first = board[0][0];
		char second = first == 'B' ? 'W':'B';
		int min = n*m;
		for (int i = 0; i <= board.length - 8; i++) {
			for (int j = 0; j <= board[0].length - 8; j++) {
				int result;
				result = count(i, j, first);
				if(result < min) min = result;
				result = count(i, j, second);
				if(result < min) min = result;
			}
		}
		System.out.println(min);
	}
	
	static int count(int a, int b, char base) {
		int cnt = 0;
		for (int i = a; i < a+8; i++) {
			for (int j = b; j < b+8; j++) {
				if(i%2 == 0) {
					if(j%2 == 0) {
						if(board[i][j] != base) {
							cnt++;
						}
					} else {
						if(board[i][j] == base) {
							cnt++;
						}
					}
				} else {
					if(j%2 == 0) {
						if(board[i][j] == base) {
							cnt++;
						}
					} else {
						if(board[i][j] != base) {
							cnt++;
						}
					}
					
				}
			}
		}
		return cnt;
	}

}
