package zwy.datatype;

import java.util.Iterator;

public class SeperateChainingHashST<K, V> extends SymbolTable<K, V>{

		private int m;
		private SequentialSearchSymbolTable<K, V>[] st;

		public SeperateChainingHashST(){
			this(997);
		}

		public SeperateChainingHashST(int m){
			super();
			this.m = m;
			st = (SequentialSearchSymbolTable<K, V>[])new SequentialSearchSymbolTable[m];
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
			/*
			 *
			 *
			 */
			int h = hash(key);
			if(!st[h].contains(key)){
				n++;
			}
			st[h].put(key, val);
		}

		public void delete(K key){
			/*
			 *
			 *
			 */
			if(!st[h].contains(key)){
				n++;
			}
			st[hash(key)].delete(key);
			n--;
		}

		public boolean contains(K key){
			return st[hash(key)].contains(key);
		}

		public Iterable<K> keys(){
			return new Iterable<K>(){
				public Iterator<K> iterator(){
					return new Iterator<K>(){

						private int currList = 0;
						private Iterator<K> currIter = st[currList].keys().iterator();

						public boolean hasNext(){
							if(!currIter.hasNext()){
								while(!currIter.hasNext() && currList < m){
									currIter = st[currList].keys().iterator();
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
			};
		}
	}