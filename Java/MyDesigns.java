// 
// 
// 
//   

import java.awt.*; //gives access to java command libraries
 //gives access to Console class file

public class MyDesigns //creates a new class called MyDesigns
{
         // creates an instance variable of Console class 
    public static void format() // drawTitle method
    {
      System.out.println();
      for (int i = 1; i <= 36; i++) {
        System.out.print(' ');
      }
    }

    public static void drawTitle() // drawTitle method
    {
      format();
      System.out.println();
      System.out.print("Designs\n");
    }

    }

    public static void drawRectangle() // drawRectangle method
    {
      format();


      // the commands to create the RECTANGLE design go in here!       
    }
    
    public void drawTrapezoid() //drawTrapezoid method
    {
      // the commands to create the TRAPEZOID design go in here!         
    }
    
    public MyDesigns() //myDesigns class constructor
    {
	 //creates a new Console object window
    }
    
    public static void main (String[] args) //main method of a Java application
    {
	MyDesigns d; //creates instance variable of MyDesigns
	d = new MyDesigns(); //constructs a new MyDesigns object
	d.drawTitle(); //executes drawTitle method
	d.drawRectangle(); //executes drawRectangle method
	d.drawTrapezoid(); //executes drawTrapezoid method
    }  
} 
