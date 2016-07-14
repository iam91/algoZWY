package zwy.datatype;

import java.util.Iterator;

public class AdjacencyListGraph extends Graph{
	private LinkedListBag<Integer>[] adj;

	public AdjacencyListGraph(int v){
		super(v);
		adj = (LinkedListBag<Integer>[])new LinkedListBag[v];
		for(int i = 0; i < v; i++){
			adj[i] = new LinkedListBag<Integer>();
		}
	}

	public AdjacencyListGraph(int v, int e, int[] a, int[] b){
		this(v);
		for(int i = 0; i < e; i++){
			addEdge(a[i], b[i]);
		}
	}

	public void addEdge(int a, int b){
		adj[a].add(b);
		adj[b].add(a);
		setE(E() + 1);
	}

	public Iterable<Integer> adj(int v){
		return adj[v];
	}
	
	public String toString(){
		String s = V() + " vertices, " + E() + " edges.\n";
		int v = V();
		for(int i = 0; i < v; i++){
			LinkedListBag<Integer> curr = adj[i];
			Iterator<Integer> iter = curr.iterator();
			s += (i + ": ");
			while(iter.hasNext()){
				s += iter.next() + " ";
			}
			s += "\n";
		}
		return s;
	}
}