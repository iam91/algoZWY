public class Temp{
	public static void main(String[] args){
		Integer[] a = {1, 5, 5, 0, 2, 6};
		Integer[] b = {1, 5, 5, 0, 2, 6};
		Integer[] c = {1, 5, 5, 0, 2, 6};
		Integer[] d = {1, 5, 5, 0, 2, 6};
		SortClient.sort(a, SortClient.INSERTION);
		SortClient.sort(b, SortClient.SELECTION);
		SortClient.sort(c, SortClient.SHELL);
		SortClient.sort(d, SortClient.MERGE);
		/*
		for(int i = 0; i < a.length; i++){
			System.out.println(a[i]);
		}
		System.out.println("---");
		for(int i = 0; i < b.length; i++){
			System.out.println(b[i]);
		}
		System.out.println("---");
		for(int i = 0; i < b.length; i++){
			System.out.println(c[i]);
		}
		System.out.println("---");*/
		for(int i = 0; i < b.length; i++){
			System.out.println(d[i]);
		}
		System.out.println("---");
	}
}