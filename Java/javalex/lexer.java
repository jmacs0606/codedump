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