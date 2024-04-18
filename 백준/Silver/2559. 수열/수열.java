import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int arr[] = new int[n];
		int maxVal = 0;
		int nowVal = 0;
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i = 0; i < k; i++) {
			nowVal += arr[i];
		}
		
		maxVal = nowVal;
		for (int i = k; i < n; i++) {
			nowVal = nowVal + arr[i] - arr[i-k];
			maxVal = Math.max(maxVal, nowVal);
		}
		
		System.out.println(maxVal);
	}

}