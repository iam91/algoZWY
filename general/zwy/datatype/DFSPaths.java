package zwy.datatype;

import java.util.Iterator;

public class DFSPaths extends Paths{
	private boolean[] visited;
	private int[] pathTo;
	private final int s;

	public DFSPaths(Graph graph, int s){
		visited = new boolean[graph.V()];
		pathTo = new int[graph.V()];
		this.s = s;
		dfs(graph, s);
	}

	private void dfs(Graph graph, int s){
		visited[s] = true;
		Iterator<Integer> iter = graph.adj(s).iterator();
		while(iter.hasNext()){
			int currNeighbor = iter.next();
			if(!visited[currNeighbor]){
				dfs(graph, currNeighbor);
				pathTo[currNeighbor] = s;
			}
		}
	}

	public boolean hasPathTo(int v){
		return visited[v];
	}

	public Iterable<Integer> pathTo(int v){
		if(!hasPathTo(v)){
			return null;
		}
		int curr = v;
		Stack<Integer> stack = new LinkedListStack<Integer>();
		stack.push(v);
		while(curr != s){
			stack.push(pathTo[curr]);
			curr = pathTo[curr];
		}
		return stack;
	}
}