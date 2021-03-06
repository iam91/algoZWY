package zwy.datatype;

import java.util.Iterator;

public class GTest{
	public static void main(String[] args){
		int[] a = {0, 4, 0, 9, 6, 5, 0, 11, 9, 0, 7, 9, 5};
		int[] b = {5, 3, 1, 12, 4, 4, 2, 12, 10, 6, 8, 11, 3};
		AdjacencyListGraph gl = new AdjacencyListGraph(13, 13, a, b);
		AdjacencyMatrixGraph gm = new AdjacencyMatrixGraph(13, 13, a, b);

		LinkedListQueue<Integer> queue = new LinkedListQueue<Integer>();
		LinkedListStack<Integer> stack = new LinkedListStack<Integer>();

		ConnectedComponent cc = new UFConnectedComponent(gl);
		
		UnionFind uf = new UnionFind(a.length);
		for(int i = 0; i < a.length; i++){
			uf.union(a[i], b[i]);
		}

		Cycle cycle = new Cycle(gl);
		System.out.println("has cycle: " + cycle.hasCycle());
		Bipartite bipar = new Bipartite(gl);
		System.out.println("is bipartite: " + bipar.isBipartite());
		/*
		System.out.println(uf.count());
		System.out.println(uf.connected(0, 4));
		System.out.println(uf.connected(2, 12));
		System.out.println(uf.connected(7, 8));
		System.out.println(uf.connected(8, 10));
		*/
		
		System.out.println(cc.count());
		//System.out.println(cc.toString());
		System.out.println(cc.connected(0, 4));
		System.out.println(cc.connected(0, 9));
		System.out.println(cc.connected(2, 12));
		System.out.println(cc.connected(7, 8));
		System.out.println(cc.connected(8, 10));
		System.out.println(cc.id(3));
		System.out.println(cc.id(10));
		System.out.println(cc.id(8));

		
		/*
		for(int i = 0; i < a.length; i++){
			queue.enqueue(a[i]);
			stack.push(a[i]);
			System.out.println(stack.size() + "," + queue.size() + " ");
		}
		System.out.println();

		for(int i = 0; i < a.length; i++){
			queue.dequeue();
			stack.pop();
			System.out.println(stack.size() + "," + queue.size() + " ");
		}
		System.out.println();
		
		System.out.println(gl.toString());
		System.out.println("==================");
		System.out.println(gm.toString());

		Iterator<Integer> iter1 = gl.adj(9).iterator();
		Iterator<Integer> iter2 = gm.adj(9).iterator();
		while(iter1.hasNext()){
			System.out.print(iter1.next() + " ");
		}
		System.out.println();
		
		while(iter2.hasNext()){
			System.out.print(iter2.next() + " ");
		}
		System.out.println();

		Paths paths1 = new DFSPaths(gl, 0);
		if(paths1.hasPathTo(5)){
			Iterator<Integer> iter = paths1.pathTo(5).iterator();
			while(iter.hasNext()){
				System.out.print(iter.next() + " ");
			}
			System.out.println();
		}
		
		Paths paths2 = new BFSPaths(gl, 0);
		if(paths2.hasPathTo(5)){
			Iterator<Integer> iter = paths2.pathTo(5).iterator();
			while(iter.hasNext()){
				System.out.print(iter.next() + " ");
			}
			System.out.println();
		}
		*/
	}
}