package zwy.datatype;

public abstract class SymbolTable<K, V>{

	protected int n;
	
	public SymbolTable(){
		n = 0;
	}

	public abstract void put(K key, V val);
	public abstract V get(K key);
	public abstract void delete(K key);
	public abstract boolean contains(K key);
	public abstract Iterable<K> keys();
	public boolean isEmpty(){
		return n == 0;
	}
	public int size(){
		return n;
	}
}