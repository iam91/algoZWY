package zwy.datatype;

import java.util.Iterator;

public class LinkedListBag<T> extends Bag<T>{
	private Node head; 

	public LinkedListBag(){
		super();
		head = null;
	}

	public void add(T item){
		if(item == null){
			return;
		}
		head = new Node(item, head);
		setSize(size() + 1);
	}

	public Iterator<T> iterator(){
		return new Iterator<T>(){
			private Node curr = head;
			public boolean hasNext(){
				return curr != null;
			}

			public T next(){
				T ret = curr.item;
				curr = curr.next;
				return ret;
			}

			public void remove(){}
		};
	}

	private class Node{
		T item;
		Node next;
		public Node(T item, Node next){
			this.item = item;
			this.next = next;
		}
	}
}