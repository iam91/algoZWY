package zwy.datatype;

public abstract class Graph{
	public abstract void addEdge(int from, int to);
	public abstract Iterable<Integer> adj(int v);
	public abstract String toString();
}