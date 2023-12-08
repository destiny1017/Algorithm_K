import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		char str[] = sc.nextLine().toCharArray();
		for (int i = 0; i < str.length; i++) {
			int code = str[i];
			if(str[i] != ' ' && str[i] - 48 > 9) {
				if(code > 64 && code < 97) str[i] = (char) (((code+13)-65)%26+65);
				else str[i] = (char) (((code+13)-97)%26+97);
			}
		}
		System.out.println(str);
	}

}