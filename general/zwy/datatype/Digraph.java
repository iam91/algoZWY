package zwy.datatype;

public abstract class Digraph{
	private final int v;
	private int e;

	public Digraph(int v){
		this.v = v;
		e = 0;
	}

	public int V(){
		return v;
	}

	public int E(){
		return e;
	}

	protected void setE(int e){
		this.e = e;
	}

	public abstract void addEdge(int a, int b);
	public abstract Iterable<Integer> adj(int a);
	public abstract String toString();
	public abstract Digraph reverse();
}