package zwy.datatype;

import java.util.Iterator;

public class SequentialSearchSymbolTable<K, V> extends SymbolTable<K, V>{
	private Node head;

	public SequentialSearchSymbolTable(){
		super();
		head = null;
	}

	public void put(K key, V val){;
		if(key == null || val == null){
			return;
		}
		for(Node curr = head; curr != null; curr = curr.next){
			if(curr.key.equals(key)){
				curr.value = val;
				return;
			}
		}
		head = new Node(key, val, head);
		n++;
	}

	public V get(K key){
		if(key == null){
			return null;
		}
		for(Node curr = head; curr != null; curr = curr.next){
			if(curr.key.equals(key)){
				return curr.value;
			}
		}
		return null;
	}

	public void delete(K key){
		if(key == null || head == null){
			return;
		}
		if(head.key.equals(key)){
			head = head.next;
			n--;
			return;
		}
		Node curr = head;
		while(curr.next != null){
			Node currChild = curr.next;
			if(currChild.key.equals(key)){
				curr.next = currChild.next;
				currChild = null;
				n--;
				return;
			}
			else{
				curr = currChild;
			}
		}
	}
	
	public boolean contains(K key){
		if(key == null){
			return false;
		}
		for(Node curr = head; curr != null; curr = curr.next){
			if(curr.key.equals(key)){
				return true;
			}
		}
		return false;
	}

	public Iterable<K> keys(){
		return new Iterable<K>(){
			public Iterator<K> iterator(){
				return new Iterator<K>(){
					private Node curr = head;
					
					public boolean hasNext(){
						return curr != null;
					}

					public K next(){
						K ret = curr.key;
						curr = curr.next;
						return ret;
					}

					public void remove(){}
				};
			}
		};
	}

	private class Node{
		K key;
		V value;
		Node next;
		public Node(K key, V value, Node next){
			this.key = key;
			this.value = value;
			this.next = next;
		}
	}
}