
public class LetVal implements Expression {

	private String name;
	private Expression valueExpr;
	private Expression bodyExpr;

    public LetVal(String name, Expression valueExpr, Expression bodyExpr) {
    	this.name = name;
    	this.valueExpr = valueExpr;
    	this.bodyExpr = bodyExpr;
    
    }

    @Override
    public Value eval(Environment env) {
    	ActivationRecord env1 = new ActivationRecord(name, valueExpr.eval(env), env);
        return bodyExpr.eval(env1);
    }

    
    public String toString() {
        return "let val " + this.name + " = " + this.valueExpr.toString() + " in " + this.bodyExpr.toString() + " end";
    }
    

}
