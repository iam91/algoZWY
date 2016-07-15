package zwy.datatype;

import java.util.Iterator;

public class LinkedListStack<T> extends Stack<T>{
	private Node head;

	public LinkedListStack(){
		super();
		head = null;
	}

	public void push(T item){
		if(item == null){
			return;
		}
		head = new Node(item, head);
		setSize(size() + 1);
	}

	public T pop(){
		if(isEmpty()){
			return null;
		}
	    T ret = head.item;
	    head = head.next;
	    setSize(size() - 1);
	    return ret;
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