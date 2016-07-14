package zwy.datatype;

import java.util.Iterator;

public class AdjacencyMatrixGraph extends Graph{
	private boolean[][] adj;

	public AdjacencyMatrixGraph(int v){
		super(v);
		adj = new boolean[v][v];
	}

	public AdjacencyMatrixGraph(int v, int e, int[] a, int[] b){
		this(v);
		for(int i = 0; i < e; i++){
			addEdge(a[i], b[i]);
		}
	}

	public void addEdge(int a, int b){
		adj[a][b] = true;
		adj[b][a] = true;
		setE(E() + 1);
	}

	public Iterable<Integer> adj(int v){
		return new Iterable<Integer>(){
			public Iterator<Integer> iterator(){
				return new Iterator<Integer>(){
					private int curr = 0;
					private int vv = V();

					public boolean hasNext(){
						if(curr < vv && !adj[v][curr]){
							while(curr < vv && !adj[v][curr]){
								curr++;
							}
						}
						return curr < vv;
					}

					public Integer next(){
						return curr++;
					}

					public void remove(){}
				};
			}
		};
	}
	
	public String toString(){
		String s = V() + " vertices, " + E() + " edges.\n";
		int v = V();
		for(int i = 0; i < v; i++){
			s += (i + ": ");
			for(int j = 0; j < v; j++){
				if(adj[i][j]){
					s += j + " ";
				}
			}
			s += "\n";
		}
		return s;
	}
}