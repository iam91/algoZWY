package zwy.datatype;

public abstract class Bag<T> implements Iterable<T>{
	private int n;

	public Bag(){
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

	public abstract void add(T item);
}