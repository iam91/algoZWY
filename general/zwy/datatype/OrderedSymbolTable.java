package zwy.datatype;

public abstract class OrderedSymbolTable<K extends Comparable<K>, V>{

	protected int n;
	
	public OrderedSymbolTable(){
		n = 0;
	}

	public abstract void put(K key, V val);
	public abstract V get(K key);
	public abstract void delete(K key);
	public abstract boolean contains(K key);
	public abstract K min();
	public abstract K max();
	public abstract K floor(K key);
	public abstract K ceiling(K key);
	public abstract int rank(K key);
	public abstract K select(int k);
	public abstract void deleteMin();
	public abstract void deleteMax();
	public abstract int size(K lo, K hi);
	public abstract Iterable<K> keys();
	public abstract Iterable<K> keys(K lo, K hi);
	public boolean isEmpty(){
		return n == 0;
	}
	public int size(){
		return n;
	}
}