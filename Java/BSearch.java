import java.util.ArrayList;
import java.lang.Math;

public class BSearch {

    
    public static int search(int var, ArrayList myList) {
        int middleIndex = myList.size();

        return middleIndex;

    }
    

    public static void main(String[] args){
        ArrayList myList = new ArrayList();
        myList.add(1);
        System.out.println(BSearch.search(4,myList));
    }
}
