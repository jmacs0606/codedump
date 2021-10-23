import java.util.Scanner;

public class lex {

    public class lexer{

        String text;
        int currentIndex;
        int tokens[];
        
        public void run(){


        }

        public String getChar(String objText, int objCurrent){
            return Character.toString(objText.charAt(objCurrent));
        }

        public int[] stop(){
            return this.tokens;
        }


        public void advance(){
            currentIndex+=1;
            if(getChar(this.text,this.currentIndex) == "~"){
                stop();
            }



        }
    
    }

    public lex(String initName) {

    }
    
    
    


    public static void main(String args[]){

        lex.lexer myCode;
        myCode = new lex.lexer();

        System.out.println(myCode.currentIndex);
    

    }
    
}
