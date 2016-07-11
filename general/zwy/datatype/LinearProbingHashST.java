package zwy.datatype;

import java.util.Iterator;

public class LinearProbingHashST<K, V> extends SymbolTable<K, V>{

	private int m;
	private K[] keys;
	private V[] vals;

	public LinearProbingHashST(){
		this(16);
	}

	public LinearProbingHashST(int m){
		this.m = m;
		keys = (K[]) new Object[this.m];
		vals = (V[]) new Object[this.m];
	}

	private int hash(K key){
		return (key.hashCode() & 0x7fffffff) % m;
	}

	private void resize(int cap){

	}

	public void put(K key, V val){
		if(key == null || val == null){
			return;
		}
		if(2 * N >= M){
			resize(2 * M);
		}
		int i;
		for(i = hash(key); keys[i] != null; i = (i + 1) % m){
			if(keys[i].equals(key)){
				vals[i] = val;
				return;
			}
		}
		keys[i] = key;
		vals[i] = val;
		n++;
	}

	public V get(K key){
		if(key == null){
			return null;
		}
		for(int i = hash(key); keys[i] != null; i = (i + 1) % m){
			if(keys[i].equals(key)){
				return vals[i];
			}
		}
		return null;
	}
	public abstract void delete(K key);
	public abstract boolean contains(K key);
	public abstract Iterable<K> keys();
}