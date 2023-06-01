import java.util.*;
/** A ScopedMap is similar to a Map, but with nested scopes. */
public class ScopedMap<K,V> {
    private final HashMap<K,V> map;
    private final Stack<HashMap<K,V>> scope = new Stack<HashMap<K,V>>();
    private int nestingLevel;

    /** makes a ScopedMap that maps no keys to values and is set to the global scope (nesting level 0) */
    public ScopedMap() {
        map = new HashMap<K, V>();
        nestingLevel = 0;
    }

    /** sets the ScopedMap to a new scope nested inside the previous one;
        the nesting level increases by one */
    public void enterScope(){
        nestingLevel++;
        scope.push(new HashMap<K, V>());
    }

    /** exits from the current scope back to the containing one;
        the nesting level, which must have been positive, decreases by one */
    public void exitScope(){
        if (getNestingLevel() == 0)
            throw new IllegalArgumentException("The nesting level is currently 0");
        nestingLevel--;
        scope.pop();
    }

    /** puts the key/value pair in at the current scope;
        if the key is already in at the current nesting level,
        the new value replaces the old one;
        neither the key nor the value may be null */
    public void put(K key, V value) {
        if(key == null || value == null)
            throw new IllegalArgumentException("Neither the key nor the value may be null");
        
        scope.peek().put(key, value);
            
    }

    /** gets the value corresponding to the key, at the innermost scope for which there is one;
        if there is none, returns null */
    public V get(K key) {
        for (int i = nestingLevel - 1; i >= 0; i--) {
            V value = scope.get(i).get(key);
            if (value != null){
                return value;
            }
        }
        return null;
    }
    
    /** returns true if the key has a value at the current scope (ignoring surrounding ones) */
    public boolean isLocal(K key) {
    	   return scope.peek().get(key) != null;
    }
    
    /** returns the current nesting level */
    public int getNestingLevel() {
    	return nestingLevel;
    }
}
