
import java.util.Scanner;

public class Main {
	
	static int cost[][];
	static int dp[][];
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		cost = new int[n][3];
		dp = new int[n][3];
		for (int i = 0; i < cost.length; i++) {
			cost[i][0] = sc.nextInt();
			cost[i][1] = sc.nextInt();
			cost[i][2] = sc.nextInt();
		}
		
		dp[0][0] = cost[0][0];
		dp[0][1] = cost[0][1];
		dp[0][2] = cost[0][2];
		
		n -= 1;
		
		System.out.println(Math.min(Math.min(recursive(n, 0), recursive(n, 1)), recursive(n, 2)));
		
	}
	
	static int recursive(int n, int color) {
		if(dp[n][color] == 0) {
			if(color == 0) {
				dp[n][0] = Math.min(recursive(n-1, 1), recursive(n-1, 2)) + cost[n][0]; 
			} else if(color == 1) {
				dp[n][1] = Math.min(recursive(n-1, 0), recursive(n-1, 2)) + cost[n][1];
			} else if(color == 2) {
				dp[n][2] = Math.min(recursive(n-1, 0), recursive(n-1, 1)) + cost[n][2];
			}
		}
		return dp[n][color];
	}

}
