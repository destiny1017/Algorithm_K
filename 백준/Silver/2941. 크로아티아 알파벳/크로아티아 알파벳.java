import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String arr[] = {"c=","c-","dz=","d-","lj","nj","s=","z="};
		String word = sc.next();
		int cnt = 0;
		for (int i = 0; i < arr.length; i++) {
			while(0 <= word.indexOf(arr[i])) {
				cnt++;
				word = word.replaceFirst(arr[i],"?");
			}
		}
		for (int i = 0; i < word.length(); i++) {
			if(!word.substring(i,i+1).equals("?")) cnt++;
		}
		System.out.println(cnt);
		
	}

}
