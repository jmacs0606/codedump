//MacLaren Scott


import java.awt.*;


public class format {
    public static void drawTitle(){ //draws the title
        formatSpace();
        System.out.print(" Designs");
    }
    public static void formatSpace() // moves the cursor to the middle of the screen
    {
        System.out.println();
        for (int i = 1; i <= 36; i++) {
            System.out.print(' ');
        }
    }

    public static void drawRect() { //draws the Rectangle
        System.out.print("\n\n\n\n\n"); //creates 5 newlines for vertical space
        formatSpace();
        System.out.print("RECTANGLE\n");
        formatSpace();
        System.out.print("E       L\n");
        formatSpace();
        System.out.print("C       G\n");
        formatSpace();
        System.out.print("T       N\n");
        formatSpace();
        System.out.print("A       A\n");
        formatSpace();
        System.out.print("N       T\n");
        formatSpace();
        System.out.print("G       C\n");
        formatSpace();
        System.out.print("L       E\n");
        formatSpace();
        System.out.print("ELGNATCER\n");
    }
    public static void drawTrap() //draws treapezoid
    {   
        System.out.print("\n\n\n\n\n"); //creates 5 newlines for vertical space
        formatSpace();
        System.out.print("  ");
        System.out.print("APEZO");
        System.out.print("    \n");
        formatSpace();
        System.out.print(" ");
        System.out.print("R     I");
        System.out.print("  \n");
        formatSpace();
        System.out.print("TRAPEZOID\n");

    }
    public static void main(String[] args) // Main method: Calls each method 
    {
        drawTitle();
  
        drawRect();

        drawTrap();

    }
}
