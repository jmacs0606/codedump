public class hello {



    public static void main(String[] args) {
        myObject myInstance = new myObject("Mike");
    }
    

}

public class myObject{
    String objName;
    int age;

    public myObject(String name){
        this.objName = name;
    }
}