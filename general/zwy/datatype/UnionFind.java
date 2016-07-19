package zwy.datatype;

public class UnionFind{
	private int[] id;
	private int count;

	public UnionFind(int n){
		count = n;
		id = new int[n];
		for(int i = 0; i < n; i++){
			id[i] = i;
		}
	}

	public void union(int p, int q){

	}

	public int find(int p){
		return 0;
	}

	public boolean connected(int p, int q){
		return find(p) == find(q);
	}

	public int count(){
		return 0;
	}
}