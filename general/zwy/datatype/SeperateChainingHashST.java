package zwy.datatype;

import java.util.Iterator;

public class SeperateChainingHashST<K, V> extends SymbolTable<K, V>{

		private int m;
		private int n;
		private SequentialSearchSymbolTable<K, V>[] st;

		public SeperateChainingHashST(){
			this(997);
		}

		public SeperateChainingHashST(int m){
			this.n = 0;
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
			if(key == null){
				return null;
			}
			return st[hash(key)].get(key);
		}

		public void put(K key, V val){
			if(key == null || val == null){
				return;
			}
			SequentialSearchSymbolTable<K, V> list = st[hash(key)];
			n -= list.size();
			list.put(key, val);
			n += list.size();
		}

		public void delete(K key){
			if(key == null){
				return;
			}
			SequentialSearchSymbolTable<K, V> list = st[hash(key)];
			n -= list.size();
			list.delete(key);
			n += list.size();
		}

		public boolean contains(K key){
			if(key == null){
				return false;
			}
			return st[hash(key)].contains(key);
		}

		public void p(){
			for(int i = 0; i < m; i++){
				Iterator<K> iter = st[i].keys().iterator();
				while(iter.hasNext()){
					System.out.print(iter.next() + " ");
				}
				System.out.println();
			}
		}

		public Iterable<K> keys(){
			return new Iterable<K>(){
				public Iterator<K> iterator(){
					return new Iterator<K>(){

						private int nextList = 1;
						private Iterator<K> currIter = st[0].keys().iterator();

						public boolean hasNext(){
							if(!currIter.hasNext()){
								while(!currIter.hasNext() && nextList < m){
									currIter = st[nextList].keys().iterator();
									nextList++;
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

		public boolean isEmpty(){
			return n == 0;
		}

		public int size(){
			return n;
		}
	}