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
	}
}