package zwy.datatype;

import java.util.Iterator;

public class AdjacencyListDigraph extends Digraph{
	private LinkedListBag<Integer>[] adj;

	public AdjacencyListDigraph(int v){
		super(v);
		adj = (LinkedListBag<Integer>[])new LinkedListBag[v];
		for(int i = 0; i < v; i++){
			adj[i] = new LinkedListBag<Integer>();
		}
	}

	public AdjacencyListDigraph(int v, int e, int[] from, int[] to){
		this(v);
		for(int i = 0; i < e; i++){
			addEdge(from[i], to[i]);
		}
	}

	public void addEdge(int from, int to){
		adj[from].add(to);
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

	public AdjacencyListDigraph reverse(){
		AdjacencyListDigraph r = new AdjacencyListDigraph(V());
		for(int i = 0; i < V(); i++){
			for(int neighbor: adj(i)){
				r.addEdge(neighbor, i);
			}
		}
		return r;
	}
}