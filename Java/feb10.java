public class feb10 {

    
    public static void draw(int[] arr){
        int[] list =  arr; 
        int i =0;
        while (i<list.length){

            if (list[i] == 1){
                System.out.print("X");
            }

            else{
                System.out.print(" ");
            }

            if ((i+1) % 5 == 0){
                System.out.print("\n");
            }

            i = i+1;
        }
    }

    public static void main(String[] args)
    {   
        int[] xLetter = {1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1}; //list for the letter x on a 5x5 canvas
        int[] mLetter = {0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,1,0,0,0,1,1,0,0,0,1};
    
        //draw(xLetter);   
        //System.out.print("\n");
        draw(mLetter);   

    }
}
    
    
   

