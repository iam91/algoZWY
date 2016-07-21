package zwy.datatype;

public class DigTest{
	public static void main(String[] args){
		int from[] = {4, 2, 3, 6, 0, 2, 11, 12, 9, 9, 8, 10, 11, 4, 3, 7, 8, 5, 0, 6, 6, 7};
		int to[] = {2, 3, 2, 0, 1, 0, 12, 9, 10, 11, 9, 12, 4, 3, 5, 8, 7, 4, 5, 4, 9, 6};
		int f[] = {0, 0, 2, 2, 3, 5, 0, 6, 7, 8, 6, 9, 9, 9, 11, 4};
		int t[] = {1, 5, 0, 3, 5, 4, 6, 4, 6, 7, 9, 10, 12, 11, 12,3};
		AdjacencyListDigraph gl = new AdjacencyListDigraph(13, 16, f, t);

		System.out.println(gl.toString());
		DirectedCycle d = new DirectedCycle(gl);
		DepthFirstOrder dfo = new DepthFirstOrder(gl);
		if(d.hasCycle()){
			for(int i: d.cycle()){
				System.out.print(i + " ");
			}
		}
		System.out.println();
		for(int i: dfo.pre()){
			System.out.print(i + " ");
		}
		System.out.println();
		for(int i: dfo.post()){
			System.out.print(i + " ");
		}
		System.out.println();
		for(int i: dfo.reversePost()){
			System.out.print(i + " ");
		}
		System.out.println();
	}
}