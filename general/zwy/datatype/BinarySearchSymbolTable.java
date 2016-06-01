package zwy.datatype;

import zwy.util.Util;

import java.util.Iterator;
import java.lang.reflect.Array;

public class BinarySearchSymbolTable<K extends Comparable<K>, V> 
	extends OrderedSymbolTable<K, V>{

	private K[] keys;
	private V[] values;

	public BinarySearchSymbolTable(){
		super();
		keys = (K[])new Comparable[1];
		values = (V[])new Object[1];
	}

	public void put(K key, V val){
		if(key == null || val == null){
			return;
		}
		int r = rank(key);
		if(r < n && keys[r].compareTo(key) == 0){
			values[r] = val;
		}
		else{
			n++;
			keys = (K[])resize(keys, n);
			values = (V[])resize(values, n);
			for(int i = n - 1; i > r; i--){
				keys[i] = keys[i - 1];
				values[i] = values[i - 1];
			}
			keys[r] = key;
			values[r] = val;
		}
	}

	public V get(K key){
		if(key == null){
			return null;
		}
		int r = rank(key);
		if(r < n && key.compareTo(keys[r]) == 0){
			return values[r];
		}
		else{
			return null;
		}
	}
	
	public void delete(K key){
		if(key == null){
			return;
		}
		int r = rank(key);
		if(r < n && key.compareTo(keys[r]) == 0){
			for(int i = r; i < n - 1; i++){
				keys[i] = keys[i + 1];
				values[i] = values[i + 1];
			}
			keys[n - 1] = null;
			values[n - 1] = null;
			n--;
			keys = (K[])resize(keys, n);
			values = (V[])resize(values, n);
		}
	}
	
	public boolean contains(K key){
		if(key == null){
			return false;
		}
		int r = rank(key);
		if(r < n && key.compareTo(keys[r]) == 0){
			return true;
		}
		return false;
	}
	
	public K min(){
		if(n == 0){
			return null;
		}
		return keys[0];
	}
	
	public K max(){
		if(n == 0){
			return null;
		}
		return keys[n - 1];
	}
	
	public K floor(K key){
		if(key == null){
			return null;
		}
		int r = rank(key);
		if(r < n && key.compareTo(keys[r]) == 0){
			return keys[r];
		}
		else{
			return keys[r - 1];
		}
	}
	
	public K ceiling(K key){
		if(key == null){
			return null;
		}
		int r = rank(key);
		if(r < n){
			return keys[r];
		}
		else{
			return null;
		}
	}
	
	public int rank(K key){
		int i = 0;
		int j = n - 1;
		while(i <= j){
			int mid = i + (j - i) / 2;
			int cmp = key.compareTo(keys[mid]);
			if(cmp < 0){
				j = mid - 1;
			}
			else if(cmp > 0){
				i = mid + 1;
			}
			else{
				return mid;
			}
		}
		return i;
	}
	
	public K select(int k){
		return keys[k];
	}
	
	public void deleteMin(){
		if(n > 0){
			for(int i = 0; i < n; i++){
				keys[i] = keys[i + 1];
				values[i] = values[i + 1];
			}
			keys[n - 1] = null;
			values[n - 1] = null;
			n--;
			keys = (K[])resize(keys, n);
			values = (V[])resize(values, n);
		}
	}
	
	public void deleteMax(){
		if(n > 0){
			keys[n - 1] = null;
			values[n - 1] = null;
			n--;
			keys = (K[])resize(keys, n);
			values = (V[])resize(values, n);
		}
	}
	
	public int size(K lo, K hi){
		if(lo == null || hi == null || hi.compareTo(lo) <= 0){
			return 0;
		}
		int rlo = rank(lo);
		int rhi = rank(hi);
		if(rhi >= n || hi.compareTo(keys[rhi]) != 0){
			rhi--;
		}
		return rhi - rlo + 1;
	}

	public Iterable<K> keys(){
		return new Iterable<K>(){
			public Iterator<K> iterator(){
				return new Iterator<K>(){
					
					private int curr = 0;

					public boolean hasNext(){
						return curr < n;
					}

					public K next(){
						return keys[curr++];
					}

					public void remove(){}
				};
			}
		};
	}

	public Iterable<K> keys(K lo, K hi){
		if(lo == null || hi == null || hi.compareTo(lo) <= 0){
			return null;
		}
		return new Iterable<K>(){
			public Iterator<K> iterator(){
				return new Iterator<K>(){

					private int rlo = rank(lo);
					private int prehi = rank(hi);
					private int rhi = 
						(prehi >= n || hi.compareTo(keys[prehi]) != 0) ? prehi - 1: prehi;
					private int curr = rlo;

					public boolean hasNext(){
						return curr <= rhi;
					}

					public K next(){
						return keys[curr++];
					}

					public void remove(){}
				};
			}
		};
	}

	private Object resize(Object arr, int n){
		Class cl = arr.getClass();
		if(!cl.isArray()){
			return null;
		}
		Class componentType = cl.getComponentType();
		int len = Array.getLength(arr);
		int newLen = 0;
		if(n > len){
			newLen = len * 2;
		}
		else if(n <= len / 4){
			newLen = len / 2;
		}
		else if(n <= len){
			return arr;
		}
		Object newArray = Array.newInstance(componentType, newLen);
		System.arraycopy(arr, 0, newArray, 0, newLen > len ? len : newLen);
		return newArray;
	}
}