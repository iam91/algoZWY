package zwy.datatype;

public class DepthFirstOrder{
	private boolean visited[];
	private Queue<Integer> pre;
	private Queue<Integer> post;
	private Stack<Integer> reversePost;

	public DepthFirstOrder(Digraph graph){
		int v = graph.V();
		pre = new LinkedListQueue<Integer>();
		post = new LinkedListQueue<Integer>();
		reversePost = new LinkedListStack<Integer>();
		visited = new boolean[v];
		for(int i = 0; i < v; i++){
			if(!visited[i]){
				dfs(graph, i);
			}
		}
	}

	public Iterable<Integer> pre(){
		return pre;
	}

	public Iterable<Integer> post(){
		return post;
	}

	public Iterable<Integer> reversePost(){
		return reversePost;
	}

	private void dfs(Digraph graph, int s){
		pre.enqueue(s);
		visited[s] = true;
		for(int neighbor: graph.adj(s)){
			if(!visited[neighbor]){
				dfs(graph, neighbor);
			}
		}
		post.enqueue(s);
		reversePost.push(s);
	}
}