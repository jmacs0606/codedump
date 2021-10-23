//MacLaren Scott
//Feb 25
//Ms Basaraba



import java.util.Scanner;

public class MyData { // main class
    public String first;
    public String middle; //vars
    public String last;
    public int houseNumber;
    public String streetName;
    public String city;
    public String zipCode;
    public int birthYear;
    public int currentYear = 2021;
    public int age;
    public String province;





    public void askData(){ //input method
        Scanner myScanner = new Scanner(System.in);
        System.out.println("What is your first name?: ");
        this.first = myScanner.nextLine();
        System.out.println("What is your middle name?: ");
        this.middle = myScanner.nextLine();
        System.out.println("What is your last name?: ");
        this.last = myScanner.nextLine();
        System.out.println("What is your house number?: ");
        this.houseNumber = myScanner.nextInt();
        System.out.println("What is your street name?: ");
        this.streetName = myScanner.nextLine();
        this.streetName = myScanner.nextLine();
        System.out.println("What is your city?: ");
        this.city = myScanner.nextLine();
        System.out.println("What is your province?: ");
        this.province= myScanner.nextLine();
        System.out.println("What is your zip code?: ");
        this.zipCode = myScanner.nextLine();
        System.out.println("What is your birthyear?: ");
        this.birthYear = myScanner.nextInt();
        this.age = this.currentYear-this.birthYear;
        
        myScanner.close();

    }

    public void displayData(){ //display method
        System.out.println("\n\n");
        System.out.print(String.format("%70s", " "));
        System.out.printf("%s %s %s\n\n", this.first, this.middle, this.last);
        System.out.print(String.format("%70s", " "));
        System.out.printf("%d %s\n\n", this.houseNumber, this.streetName);
        System.out.print(String.format("%70s", " "));
        System.out.printf("%s, %s, %s\n\n\n\n", this.city, this.province, this.zipCode);
        System.out.print(String.format("%70s", " "));
        System.out.printf("You are: %d years old.\n\n\n", this.age);
        System.out.print(String.format("%70s", " "));
    }
    public static void main(String[] args) { //main method
        MyData mainObj = new MyData();  //constructor


        mainObj.askData(); //calling methods
        mainObj.displayData();
    }
}
