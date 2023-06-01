
public class LetFun implements Expression {

    private String functionName;
    private String parameter;
    private Expression functionBody;
    private Expression letBody;

    public LetFun(String functionName, String parameter, Expression functionBody,
            Expression letBody) {
        this.functionName = functionName;
        this.parameter = parameter;
        this.functionBody = functionBody;
        this.letBody = letBody;
    }

    @Override
    public Value eval(Environment env) {
        ActivationRecord env1 = new ActivationRecord (functionName, parameter, functionBody, env);
        return letBody.eval(env1);
    }

    
    public String toString() {
        return "let fun "+this.functionName+" "+this.parameter+" = "+this.functionBody.toString()+" in "+this.letBody.toString()+" end";
    }
    

}
