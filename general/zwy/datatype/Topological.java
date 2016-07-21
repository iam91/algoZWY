package zwy.datatype;

public class Topological{
	private Iterable<Integer> order;
	
	public Topological(Digraph graph){
		order = null;
		DirectedCycle cycle = new DirectedCycle(graph);
		if(!cycle.hasCycle()){
			DepthFirstOrder dfo = new DepthFirstOrder(graph);
			order = dfo.reversePost();
		}
	}

	public Iterable<Integer> order(){
		return order;
	}

	public boolean isDAG(){
		return order != null;
	}
}