package zwy.datatype;

public abstract class Graph{
	
	private final int v;
	private int e;

	public Graph(int v){
		this.v = v;
		this.e = 0;
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
	public abstract Iterable<Integer> adj(int v);
	public abstract String toString();
}