import java.util.Scanner;

public class Main {
	
	static char[][] board;
	static boolean[][] visit;
	static int[] dx = {0, 0, -1, 1};
	static int[] dy = {-1, 1, 0, 0};
	static boolean blind = false;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		board = new char[n][n];
		visit = new boolean[n][n];
		
		for (int i = 0; i < n; i++) {
			char[] charStr = sc.next().toCharArray();
			for (int j = 0; j < n; j++) {
				board[i][j] = charStr[j];
			}
		}

		int normal = count();
		visit = new boolean[n][n];
		blind = true;
		int blindColor = count();
		
		System.out.println(normal + " " + blindColor);
		
	}
	
	public static int count() {
		int cnt = 0;
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board.length; j++) {
				if(!visit[i][j]) {
					dfs(i, j);
					cnt++;
				}
			}
		}
		return cnt;
	}
	
	public static void dfs(int n, int m) {
		visit[n][m] = true;
		
		for (int i = 0; i < 4; i++) {
			int nx = n + dx[i];
			int ny = m + dy[i];
			
			if(nx >= 0 && ny >= 0 && nx < board.length && ny < board.length) {
				// 색맹일 경우
				if(blind) {
					if(board[n][m] == 'B') {
						if(!visit[nx][ny] && board[nx][ny] == board[n][m]) {
							dfs(nx, ny);
						}
					} else {
						if(!visit[nx][ny] && board[nx][ny] != 'B') {
							dfs(nx, ny);
						}
					}
					
				// 색맹이 아닐 경우
				} else {
					if(!visit[nx][ny] && board[nx][ny] == board[n][m]) {
						dfs(nx, ny);
					}
				}
			}
		}
	}

}
