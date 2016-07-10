package zwy.datatype;

import java.util.Iterator;

public class SeperateChainingHashST<K, V> extends SymbolTable<K, V>{

		private int m;
		private SequentialSearchST<K, V>[] st;

		public SeperateChainingHashST(){
			this(997);
		}

		public SeperateChainingHashST(int m){
			super();
			this.m = m;
			st = new SequentialSearchSymbolTable<K, V>[m];
			for(int i = 0; i < m; i++){
				st[i] = new SequentialSearchSymbolTable<K, V>();
			}
		}

		private int hash(K key){
			return (key.hashCode() & 0x7fffffff) % m;
		}

		public V get(K key){
			return st[hash(key)].get(key);
		}

		public void put(K key, V val){
			st[hash(key)].put(key, val);
			n++;
		}

		public void delete(K key){
			st[hash(key)].put(key);
			n--;
		}

		public boolean contains(K key){
			return st[hash(key)].contains(key);
		}

		public Iterable<K> keys(){
			public Iterator<K> iterator(){
				return new Iterator<K>(){

					private int currList = 0;
					private Iterable<K> currIter = st[currList].keys();

					public boolean hasNext(){
						if(!currIter.hasNext()){
							while(!currIter.hasNext() && currList < m){
								currIter = st[currList].keys();
								currList++;
							}
						}
						return currIter.hasNext();
					}

					public K next(){
						return currIter.next();
					}

					public void remove(){}
				};
			}
		}
	}