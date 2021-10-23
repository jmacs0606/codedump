//MacLaren Scott

//To run and compile:
//javac TestMarks.java
//java TestMarks

public class TestMarks {
    
    public static void space(){ //this method prints one tab
        System.out.print("\t"); //prints a tab to center
    }

    public static void drawTitle(){
        System.out.print("\n"); // prints top margin
        System.out.print("\n");

        space();  //prints the first row that has headers
        space();
        System.out.print("Student");
        space();
        space();
        System.out.print("Test 1");
        space();
        space();
        System.out.print("Test 2");
        space();
        space();
        System.out.print("Test Average");
        space();
        space();

    }

    public static void displayMarks(){
        System.out.print("\n"); //prints two newlines
        System.out.print("\n");

        space();
        space();
        System.out.print("Ali");
        space();
        space();
        System.out.print("78");
        space();
        space();
        System.out.print("62");
        space();
        space();
        System.out.print(((78 + 62))/2); // calculates average (float division)
        System.out.print(".00"); //appends trailing decimals
        space();
        space();

        System.out.print("\n");

        space();
        space();
        System.out.print("Mia");
        space();
        space();
        System.out.print("59");
        space();
        space();
        System.out.print("70");
        space();
        space();
        System.out.print(((59.00 + 70)/2)); // calculates average (float division)
        System.out.print("0"); //appends trailing decimals
        space();
        space();

        System.out.print("\n");

        space();
        space();
        System.out.print("Ned");
        space();
        space();
        System.out.print("82");
        space();
        space();
        System.out.print("73");
        space();
        space();
        System.out.print(((82.00 + 73.00)/2)); // calculates average (float division)
        System.out.print("0"); //appends trailing decimals
        space();
        space();

        System.out.print("\n"); //prints bottom margin
        System.out.print("\n");
        System.out.print("\n");
    }


    public static void main(String[] args) {
        drawTitle();
        displayMarks();
    }
}