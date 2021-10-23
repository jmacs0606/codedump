

import java.util.Scanner;

public class AncientMarriage {

	public static int[][] getData() {
		int[] height = {0,0};
		int[] age = {0,0};
		Scanner s = new Scanner(System.in);
		System.out.println("What is the mans height?  ");
		height[0] = s.nextInt();
		System.out.println("What is the womans height?  ");
		height[1] = s.nextInt();
		System.out.println("What is the mans age?  ");
		age[0] = s.nextInt();
		System.out.println("What is the womans age?  ");
		age[1] = s.nextInt();

		s.close();
		
		return new int[][] {height,age};
	}
	public static String makeDecision(int[][] data) {
		int heightDif = Math.abs(data[0][1]-data[0][0]);
		int ageDif = Math.abs(data[1][1]-data[1][0]);
		if(heightDif <= 20 && heightDif >= 5 && ageDif <=4 && data[1][0] > 18 && data[1][1] > 18) {
			return "Happy and long lasting";
		}
		else {
			return "Probably not";
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
			int[][] data = getData();
			System.out.println(makeDecision(data));
	}

}
