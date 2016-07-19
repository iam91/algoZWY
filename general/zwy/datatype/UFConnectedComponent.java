package zwy.datatype;

public class UFConnectedComponent extends ConnectedComponent{
	private UnionFind uf;
	private int count;

	public UFConnectedComponent(Graph graph){
		int v = graph.V();
		uf = new UnionFind(v);
		for(int i = 0; i < v; i++){
			for(int neighbor: graph.adj(i)){
				uf.union(i, neighbor);
			}
		}
		count = uf.count();
	}

	public boolean connected(int a, int b){
		return uf.connected(a, b);
	}
	
	public int count(){
		return count;
	}
	
	public int id(int a){
		return uf.find(a);
	}
} 