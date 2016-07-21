package zwy.datatype;

public class Cycle{
	private boolean[] visited;
	private boolean hasCycle;

	public Cycle(Graph graph){
		int v = graph.V();
		visited = new boolean[v];
		for(int i = 0; i < v; i++){
			if(!visited[i]){
				dfs(graph, i, i);
			} 
		}
	}

	public boolean hasCycle(){
		return hasCycle;
	}

	private void dfs(Graph graph, int s, int c){
		visited[c] = true;
		for(int neighbor: graph.adj(c)){
			if(hasCycle){
				return;
			}
			if(!visited[neighbor]){
				dfs(graph, c, neighbor);
			}
			else if(neighbor != s){
				hasCycle = true;
				return;
			}
		}
	}
}