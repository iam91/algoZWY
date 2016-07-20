package zwy.datatype;

public class Bipartite{
	private boolean[] visited;
	private boolean[] color;
	private boolean isBipartite;

	public Bipartite(Graph graph){
		int v = graph.V();
		visited = new boolean[v];
		color = new boolean[v];
		isBipartite = true;
		for(int i = 0; i < v; i++){
			if(!visited[i]){
				dfs(graph, i);
			}
		}
	}

	public boolean isBipartite(){
		return isBipartite;
	}

	private void dfs(Graph graph, int s){
		visited[s] = true;
		for(int neighbor: graph.adj(s)){
			if(!visited[neighbor]){
				color[neighbor] = !color[s];
				dfs(graph, neighbor);
			}
			else if(color[neighbor] == color[s]){
				isBipartite = false;
				return;
			}
		}
	}
}