package javalex;

public class test {
    

    public static void main(String args[]){
        Student myStudent = new Student();
        myStudent.firstName = "Marv";
        myStudent.lastName = "Forrer";
        myStudent.major = "Art";
        myStudent.gpa = 3.0;
        myStudent.age = 22;
        myStudent.onProbation = true;

        System.out.print(myStudent.firstName);

    }

}



