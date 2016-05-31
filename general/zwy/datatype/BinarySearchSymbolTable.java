package zwy.datatype;

import java.util.Iterator;

public class BinarySearchSymbolTable<K extends Comparable<K>, V> 
	extends OrderedSymbolTable<K, V>{
	private Comparable[] seq;

	public BinarySearchSymbolTable(){
		super();
		seq = new Comparable[1];
	}

	public void put(K key, V val){
		/*
		n++;
		if(n > seq.length){
			Comparable[] newSeq = new Comparable[seq.length * 2];
			for(int i = 0; i < seq.length; i++){
				newSeq[i] = seq[i];
				seq[i] = null;
			}
			seq = newSeq;
		}
		//seq[n - 1] =
		*/ 
	}

	public V get(K key){return null;}
	
	public void delete(K key){}
	
	public boolean contains(K key){return false;}
	
	public boolean isEmpty(){return false;}
	
	public int size(){return 0;}
	
	public K min(){return null;}
	
	public K max(){return null;}
	
	public K floor(K key){return null;}
	
	public K ceiling(K key){return null;}
	
	public int rank(K key){return 0;}
	
	public K select(int k){return null;}
	
	public void deleteMin(){}
	
	public void deleteMax(){}
	
	public int size(K lo, K hi){return 0;}

	private class Node{

	}
}