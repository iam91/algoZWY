package zwy.datatype;

import java.util.Iterator;

public class LinkedListQueue<T> extends Queue<T>{
	private Node head;
	private Node tail;

	public LinkedListQueue(){
		super();
		head = null;
		tail = null;
	}

	public void enqueue(T item){
		if(item == null){
			return;
		}
		if(tail == null){
			tail = new Node(item, null);
		}
		else{
			tail.next = new Node(item, null);
			tail = tail.next;
		}
		if(head == null){
			head = tail;
		}
		setSize(size() + 1);
	}

	public T dequeue(){
		if(isEmpty()){
			return null;
		}
		T ret = head.item;
		head = head.next;
		if(head == null){
			tail = null;
		}
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