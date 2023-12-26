import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int len = sc.nextInt();
		int price = sc.nextInt();
		int coin[] = new int[len];
		int cnt = 0;
		for (int i = 0; i < len; i++) coin[i] = sc.nextInt();
		while(price > 0) {
			for (int i = coin.length-1; i >= 0; i--) {
				int value = price / coin[i];
				if(price / coin[i] > 0) {
					cnt += value;
					price -= coin[i] * value;
				}
			}
		}
		System.out.println(cnt);
	}

}