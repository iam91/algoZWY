package zwy.datatype;

public class DirectedCycle{
	private boolean[] visited;
	private boolean[] onStack;
	private boolean hasCycle;
	private int[] edgeTo;
	private Stack<Integer> cycle;
	private int v;

	public DirectedCycle(Digraph graph){
		v = graph.V();
		visited = new boolean[v];
		onStack = new boolean[v];
		hasCycle = false;
		edgeTo = new int[v];
		cycle = null;
		for(int i = 0; i < v; i++){
			if(!visited[i]){
				dfs(graph, i);
			}
		}
	}

	boolean hasCycle(){
		return hasCycle;
	}

	Iterable<Integer> cycle(){
		return cycle;
	}

	private void dfs(Digraph graph, int s){
		visited[s] = true;
		onStack[s] = true;
		for(int neighbor: graph.adj(s)){
			if(hasCycle){
				return;
			}
			if(!visited[neighbor]){
				edgeTo[neighbor] = s;
				dfs(graph, neighbor);
			}
			else if(onStack[neighbor]){
				hasCycle = true;
				cycle = (LinkedListStack<Integer>)new LinkedListStack();
				for(int i = s; i != neighbor; i = edgeTo[i]){
					cycle.push(i);
				}
				cycle.push(neighbor);
				cycle.push(s);
			}
		}
		onStack[s] = false;
	}
}