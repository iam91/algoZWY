package zwy.datatype;

public abstract class Queue<T> implements Iterable<T>{
	private int n;

	public Queue(){
		n = 0;
	}

	public int size(){
		return n;
	}

	public boolean isEmpty(){
		return n == 0;
	}

	protected void setSize(int n){
		this.n = n;
	}

	public abstract void enqueue(T item);
	public abstract T dequeue();
}