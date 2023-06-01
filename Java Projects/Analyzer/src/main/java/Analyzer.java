import java.util.*;
import java.io.*;
public class Analyzer {

	private String input;
	private int look = 0;
	private String output = "";
	private int declaration = 1;
	private int beginnings = 0;
	private int endings = 0;
	ArrayList<String> token = new ArrayList<String>();
	ScopedMap<String, Integer> analyze = new ScopedMap<String, Integer>();


	/**
	 * Construct an Analyzer.
	 */
	public Analyzer(){
	}

	/**
	 * Analyze a block and return it with indentation and scope info.
	 * @param input the block to analyze
	 */
	public String analyze(String input) {
		this.input = input;
		Scanner tokens = new Scanner(input);
		while (tokens.hasNext()) {
			
			if(tokens.hasNext("begin")) {
				beginnings++;
			}
			if(tokens.hasNext("end")) {
				endings++;
			}
			token.add(tokens.next());
		}

		if(!input.startsWith("begin") || !input.endsWith("end")) {
			throw new IllegalArgumentException ("Invalid block");
		}
		else if(beginnings!=endings) {
				throw new IllegalArgumentException("There are an uneven number of beginnings and endings of blocks");
		}
		
		else {
			blck();

			//if there are elements in the array that were not parsed there must be more input past the initial block
			if(token.size() > look) {
				throw new IllegalArgumentException("The input must contain a single block");
			}
		}

		return output;
	}

	public static void main(String[] args) throws FileNotFoundException {
        String input = new Scanner(new File(args[0])).useDelimiter("\\Z").next();
        System.out.println(new Analyzer().analyze(input));
    }

    public void blck() {
			match("begin");

			output += indent(analyze.getNestingLevel()) + "begin\n";
			analyze.enterScope();
			stmts();

			match("end");

			output += indent(analyze.getNestingLevel()-1) + "end\n";
			analyze.exitScope();
			}
	public void stmts(){

		if(token.get(look).equals("end"))
			;
		else {
			stmt();
			stmts();
		}
	}
	public void stmt(){
		if(token.get(look).equals("pass")) {
			match("pass");
			output += indent(analyze.getNestingLevel()) + "pass\n";
		}
		else if (token.get(look).equals("declare")) {
			match("declare");
			if(analyze.isLocal(token.get(look))){
				output += indent(analyze.getNestingLevel()) + "declare "+token.get(look)+" {illegal redeclaration}\n";
				look++;
			}
			else {
				output += indent(analyze.getNestingLevel()) + "declare "+token.get(look)+" {declaration "+declaration+"}\n";
				analyze.put(token.get(look), declaration);
				look++;
				declaration++;
			}
		}
		else if (token.get(look).equals("use")) {
			match("use");
			if(analyze.get(token.get(look))==null){
				output += indent(analyze.getNestingLevel()) + "use "+token.get(look)+" {illegal undeclared use}\n";
				look++;
			}
			else {
				output += indent(analyze.getNestingLevel()) + "use "+token.get(look)+" {references declaration "+analyze.get(token.get(look))+"}\n";
				look++;
			}
		}
		else if (token.get(look).equals("begin")) {
			blck();
		}
		else {
			throw new IllegalArgumentException ("Illegal Statement");
		}
	}
	public void match(String lookahead) {
		if(lookahead.equals(token.get(look))) {
			look++;
		}
		else
			throw new IllegalArgumentException ("The input is invalid");
	}

	public static String indent(int x) {
		String spaces = "";
		for (int i = 0; i<x; i++) {
			spaces += "  ";
		}
		return spaces;
	}

}
