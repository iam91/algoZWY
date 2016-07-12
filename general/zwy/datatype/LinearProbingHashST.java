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
		LinearProbingHashST<K, V> t = new LinearProbingHashST<K, V>(cap);
		for(int i = 0; i < m; i++){
			if(keys[i] != null){
				t.put(keys[i], vals[i]);
			}
		}
		keys = t.keys;
		vals = t.vals;
		m = t.m;
	}

	public void put(K key, V val){
		if(key == null || val == null){
			return;
		}
		if(2 * n >= m){
			resize(2 * m);
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

	public void delete(K key){
		if(key == null){
			return;
		}
		int i = hash(key);
		while(!key.equals(keys[i]) && keys[i] != null){
			i = (i + 1) % m;
		}
		if(keys[i] == null){
			return;
		}
		keys[i] = null;
		vals[i] = null;
		i = (i + 1) % m;
		while(keys[i] != null){
			K keyToRedo = keys[i];
			V valToRedo = vals[i];
			keys[i] = null;
			vals[i] = null;
			n--;
			put(keyToRedo, valToRedo);
			i = (i + 1) % m;
		}
		n--;
		if(n > 0 && n <= m / 8){
			resize(m / 2);
		}
	}
	
	public boolean contains(K key){
		if(key == null){
			return false;
		}
		for(int i = hash(key); keys[i] != null; i = (i + 1) % m){
			if(keys[i].equals(key)){
				return true;
			}
		}
		return false;
	}
	
	public Iterable<K> keys(){
		return new Iterable<K>(){
			public Iterator<K> iterator(){
				return new Iterator<K>(){
					
					private int cnt = 0;
					private int curr = 0;

					public boolean hasNext(){
						return (cnt++) < n;
					}

					public K next(){
						while(curr < m && keys[curr] == null){
							curr++;
						}
						return keys[curr++];
					}

					public void remove(){}
				};
			}
		};
	}
}