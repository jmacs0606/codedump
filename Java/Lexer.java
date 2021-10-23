

import java.util.ArrayList;

class Tok{
	String type;
	String varName;
	int intVal;
	
	Tok(String type, String value){
		this.type = type;
		if(type == "var") {
			this.varName = value;
		}
		else if (type == "int") {
			this.intVal = Integer.parseInt(value);
		}
	}
}

public class Lexer {
	int lexerCurrentIndex;
	String WHITESPACE = " \t\n";
	String BREAKCHARS = ":,";
	String body;
	boolean eofReached;
	
	Lexer(String body){
		this.lexerCurrentIndex = 0;
		this.body = body;
		if(this.body.length() > 0) {
			this.eofReached = false;
		}
		else {
			this.eofReached = true;
		}
		
	}
	
	public ArrayList<Token> lex_file() {
		this.lexerCurrentIndex = 0;
		ArrayList<Token> tokenList = new ArrayList<Token>();
		//everything here
		while(!this.eofReached) {
			tokenList.add(this.lexer_get_next_token());
		}
		
		
		return tokenList;
	}
	
	public static void lexer_end_of_file() {
		System.out.println("Compilation complete.");
	}
	public void lexer_advance() {
		if(lexerCurrentIndex >= this.body.length()) {
			lexer_end_of_file();
		}
		else{
			this.lexerCurrentIndex ++;
		}
	}
	public void lexer_skip_whitespace() {
		//skips past whitespace
		while(WHITESPACE.indexOf(Character.toString(this.body.charAt(this.lexerCurrentIndex)))!=-1) { //checks if space tab or newline
			this.lexerCurrentIndex ++;
		}
	}
	
	public boolean isAlpha(String name) {
	    char[] chars = name.toCharArray();

	    for (char c : chars) {
	        if(!Character.isLetter(c)) {
	            return false;
	        }
	    }

	    return true;
	}
	
	public Tok lexer_get_next_token() {
		String tempString = "";
		this.lexer_skip_whitespace();
		if(this.lexer_check_if_char_break()) {
			tempString+= this.lexer_get_char_of_current();
			if (tempString.equals(":")) {
				return new Tok("col",null);
			}
			else if (tempString.equals("s,")) {
				return new Tok("com",null);
			}
			
		}
		while(!lexer_check_if_char_break() && WHITESPACE.contains(this.lexer_get_char_of_current())){ 	//checks if space tab or newline
			tempString += this.lexer_get_char_of_current();
			this.lexer_advance();
		}
		if (tempString.equals("i")) {
			return new Toke("int",null);
		}
		else if (tempString.equals("s")) {
			return new Token("str",null);
		}
		if(isAlpha(tempString)) {
			return new Token("var",tempString);
		}
		else if(isNumeric(this.lexer_get_char_of_current())){
			return new Token("int",tempString);
		}
		else {
			System.out.println("Uncaght error: token not identified.");
		}
		
		
		
		
	}
	
	public String lexer_get_char_of_current(){
		return Character.toString(body.charAt(this.lexerCurrentIndex)); //returns current char
	}
	public static boolean isNumeric(String str) { 
		  try {  
		    Double.parseDouble(str);  
		    return true;
		  } catch(NumberFormatException e){  
		    return false;  
		  }  
		}
	public boolean lexer_check_if_char_break() {
		String current = this.lexer_get_char_of_current();
		if(this.BREAKCHARS.contains(current)) {
			return true;
		}
		else {
			return true;
		}
	}

	public static void main(String[] args) {
		Lexer myFile = new Lexer("myString: 88,");
		ArrayList<Token> tokens = myFile.lex_file();
		
		System.out.println(tokens);

	}
}
