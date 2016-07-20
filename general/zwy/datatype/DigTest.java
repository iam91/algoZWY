package zwy.datatype;

public class DigTest{
	public static void main(String[] args){
		int from[] = {4, 2, 3, 6, 0, 2, 11, 12, 9, 9, 8, 10, 11, 4, 3, 7, 8, 5, 0, 6, 6, 7};
		int to[] = {2, 3, 2, 0, 1, 0, 12, 9, 10, 11, 9, 12, 4, 3, 5, 8, 7, 4, 5, 4, 9, 6};

		AdjacencyListDigraph gl = new AdjacencyListDigraph(13, 22, from, to);

		System.out.println(gl.toString());
	}
}