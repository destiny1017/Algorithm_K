
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	
	// 동서남북 좌표이동용 배열
	static int dx[] = {1, -1, 0, 0};
	static int dy[] = {0, 0, 1, -1};
	
	static int arr[][];
	static boolean visit[][];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer> cntList = new ArrayList<>();
		int n = sc.nextInt();
		arr = new int[n+2][n+2];
		visit = new boolean[n+2][n+2];
		for (int i = 1; i <= n; i++) {
			String line[] = sc.next().split("");
			for (int j = 1; j <= line.length; j++) {
				arr[i][j] = Integer.parseInt(line[j-1]);
			}
		}
		
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				if(arr[i][j] == 1 && visit[i][j] == false) {
					cntList.add(bfs(j, i));
				}
			}
		}
		System.out.println(cntList.size());
		Collections.sort(cntList);
		for (int i = 0; i < cntList.size(); i++) {
			System.out.println(cntList.get(i));
		}
	}
	
	static int bfs(int startX, int startY) {
		Queue<Coordinate> queue = new LinkedList<Coordinate>();
		queue.offer(new Coordinate(startX, startY));
		int cnt = 0;
		visit[startY][startX] = true;
		
		while(!queue.isEmpty()) {
			Coordinate target = queue.poll();
			cnt++;
			for (int i = 0; i < 4; i++) {
				int x = target.x + dx[i];
				int y = target.y + dy[i];
				if(arr[y][x] == 1 && visit[y][x] == false) {
					queue.offer(new Coordinate(x, y));
					visit[y][x] = true;
				}
			}
		}
		return cnt;
	}
	
	public static class Coordinate {
		int x;
		int y;
		
		public Coordinate(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
}
