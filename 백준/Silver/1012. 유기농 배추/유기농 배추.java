
import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	
	static Queue<Integer> xQueue = new LinkedList<>();
	static Queue<Integer> yQueue = new LinkedList<>();
	static int[][] board;
	static boolean[][] visit;
	static int dx[] = {-1, 1, 0, 0};
	static int dy[] = {0, 0, -1, 1};

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		// 테스트 케이스만큼 반복
		for (int i = 0; i < n; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			int h = sc.nextInt();
			int cnt = 0;
			board = new int[x][y];
			visit = new boolean[x][y];
			
			// board 데이터 삽입
			for (int j = 0; j < h; j++) {
				board[sc.nextInt()][sc.nextInt()] = 1;
			}
			
			// 전체 순회하며 방문 안된 배추노드 있으면 bfs수행
			for (int j = 0; j < x; j++) {
				for (int k = 0; k < y; k++) {
					if(!visit[j][k] && board[j][k] == 1) {
						cnt++;
						xQueue.offer(j);
						yQueue.offer(k);
						bfs();
					}
				}
			}
			board = null;
			visit = null;
			
			System.out.println(cnt);
		}
	}
	
	static void bfs() {
		while(!xQueue.isEmpty()) {
			int qx = xQueue.poll();
			int qy = yQueue.poll();
			for (int i = 0; i < 4; i++) {
				int nx = qx + dx[i];
				int ny = qy + dy[i];
				if(isValidLocation(nx, ny)) {
					xQueue.offer(nx);
					yQueue.offer(ny);
					visit[nx][ny] = true;
				}
			}
		}
	}
	
	static boolean isValidLocation(int x, int y) {
		return (x >= 0 && y >= 0 && x < board.length && y < board[0].length)
				&& !visit[x][y]
				&& board[x][y] == 1;
	}
	

}
