package zwy.datatype;

import java.util.Iterator;

public class BFSPaths extends Paths{
	private boolean[] visited;
	private int[] pathTo;
	private final int s;

	public BFSPaths(Graph graph, int s){
		visited = new boolean[graph.V()];
		pathTo = new int[graph.V()];
		this.s = s;
		bfs(graph, s);
	}

	private void bfs(Graph graph, int s){
		Queue<Integer> queue = new LinkedListQueue<Integer>();
		queue.enqueue(s);
		visited[s] = true;
		while(!queue.isEmpty()){
			int curr = queue.dequeue();
			Iterator<Integer> iter = graph.adj(curr).iterator();
			while(iter.hasNext()){
				int currNeighbor = iter.next();
				if(!visited[currNeighbor]){
					queue.enqueue(currNeighbor);
					pathTo[currNeighbor] = curr;
					visited[currNeighbor] = true;
				}
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