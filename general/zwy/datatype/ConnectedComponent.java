package zwy.datatype;

public class ConnectedComponent{
	private int[] id;
	private int count;

	public ConnectedComponent(Graph graph){
		int numOfVertices = graph.V();
		id = new int[numOfVertices];
		count = 0;
		for(int i = 0; i < numOfVertices; i++){
			id[i] = -1;
		}
		for(int i = 0; i < numOfVertices; i++){
			if(id[i] == -1){
				dfs(graph, i);
				count++;
			}
		}
	}

	public boolean connected(int a, int b){
		return id[a] == id[b];
	}

	public int count(){
		return count;
	}

	public int id(int a){
		return id[a];
	}

	public String toString(){
		String ret = "";
		for(int i = 0; i < count; i++){
			ret += (i + ": ");
			for(int j = 0; j < id.length; j++){
				if(id[j] == i){
					ret += (j + " ");
				}
			}
			ret += "\n";
		}
		return ret;
	}

	private void dfs(Graph graph, int s){
		id[s] = count;
		for(int neighbor: graph.adj(s)){
			if(id[neighbor] == -1){
				dfs(graph, neighbor);
			}
		}
	}
}