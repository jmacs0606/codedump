/*
MacLaren Scott
Basaraba
Computer Science
This code takes an input from user and creates a times table of the multiple of 7

*/


import java.util.Scanner;

public class TimesTable { //Superclass
	
	public static void title() { //title method
		System.out.println(String.format("%76s", "Times Table of Seven!\n"));
	}
	public static int askForInput(){ //input method
		Scanner s = new Scanner(System.in); //instantiates scanner
		System.out.println(("This program will ask you for a number, and will output 12 lines of the multiplication table of 4, ending with your number as the final line.\n\nWhat is your number?"));
		int in = s.nextInt();
		s.close(); //closes scanner
		System.out.print("\n\n");
		return in;
	}
	public static void displayData(int in){ //displays the table
		//displays header
		System.out.print(String.format("%24s", " "));
		System.out.print(String.format("%-30s", "Given  Number "));
		System.out.print(String.format("%-15s", "x"));
		System.out.print(String.format("%-13s", "Multiplied By "));
		System.out.println(String.format("%20s", "Answer"));
		
		//displays body
		for (int i = 1; i < 13; i++){
	
		    System.out.print(String.format("%32d",in));

		    System.out.print(String.format("%23s","x"));
		    
		    System.out.print(String.format("%22d",7));
		    
		    System.out.print(String.format("%24d",7*in));

		    in+=1;
		    System.out.println();
	}
	
	}
	
	public static void main(String[] args) { //main method
		title(); //calls title
		displayData(askForInput()-5); //uses input from input method as an argument for the display data method
		
	}
}
