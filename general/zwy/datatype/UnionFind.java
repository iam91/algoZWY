package zwy.datatype;

public class UnionFind{
	private int[] id;
	private int[] sz;
	private int count;

	public UnionFind(int n){
		count = n;
		id = new int[n];
		sz = new int[n];
		for(int i = 0; i < n; i++){
			id[i] = i;
			sz[i] = 1;
		}
	}

	public void union(int p, int q){
		int rootP = find(p);
		int rootQ = find(q);
		if(rootP != rootQ){
			if(sz[rootP] > sz[rootQ]){
				id[rootQ] = rootP;
				sz[rootP] = sz[rootP] + sz[rootQ];
			}
			else{
				id[rootP] = rootQ;
				sz[rootQ] = sz[rootP] + sz[rootQ];
			}
			count--;
		}
	}

	public int find(int p){
		int curr = p;
		while(id[curr] != curr){
			curr = id[curr];
		}
		int root = curr;
		curr = p;
		while(id[curr] != curr){
			int t = id[curr];
			id[curr] = root;
			curr = t;
		}
		return root;
	}

	public boolean connected(int p, int q){
		return find(p) == find(q);
	}

	public int count(){
		return count;
	}
}