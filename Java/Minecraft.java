import java.util.Scanner;
public class Minecraft {

	
	public static int[] getData() {
		int width;
		int height;
		Scanner s = new Scanner(System.in);
		System.out.println("What is the width?  ");
		width = s.nextInt();
		System.out.println("What is the height?  ");
		height = s.nextInt();
		s.close();
		
		return new int[] {width,height};
	}
	
	public static String verifyDims(int[] dims) {
		if(dims[0] < 24 && dims[0] > 3 && dims[1] < 24 && dims[1] > 4) {
			return "Theadore did it!";
		}
		else {
			return "Whoops, wrong again";
		}
	}

	public static void main(String[] args) {
		int[] dims = getData();
		System.out.println(verifyDims(dims));
	}

}
