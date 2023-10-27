import java.util.Scanner;
import java.util.Stack;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		char[] str = sc.nextLine().toCharArray();
		Stack<Character> stack = new Stack<>();
		boolean flag = false;
		for (int i = 0; i < str.length; i++) {
			if(str[i] == '<' || str[i] == '>' || str[i] == ' ') {
				while(!stack.isEmpty()) {
					System.out.print(stack.pop());
				}
				if(str[i] == '<') flag = true;
				else if(str[i] == '>') flag = false;
				System.out.print(str[i]);
				continue;
			}
			if(flag) {
				System.out.print(str[i]);
			} else {
				stack.push(str[i]);
			}
		}
		while(!stack.isEmpty()) {
			System.out.print(stack.pop());
		}

	}

}
