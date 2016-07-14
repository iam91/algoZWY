package zwy.datatype;

public abstract class SymbolTable<K, V>{

	public abstract void put(K key, V val);
	public abstract V get(K key);
	public abstract void delete(K key);
	public abstract boolean contains(K key);
	public abstract Iterable<K> keys();
	public abstract boolean isEmpty();
	public abstract int size();
}