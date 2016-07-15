package zwy.datatype;

public abstract class Stack<T> implements Iterable<T>{
	private int n;

	public Stack(){
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

	public abstract void push(T item);
	public abstract T pop();
}