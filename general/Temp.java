public class Temp{
	public static void main(String[] args){
		Integer[] a = {1, 5, 5, 0, 2, 6};
		Integer[] b = {1, 5, 5, 0, 2, 6};
		Integer[] c = {1, 5, 5, 0, 2, 6};
		Sort.sort(a, Sort.INSERTION);
		Sort.sort(b, Sort.SELECTION);
		Sort.sort(c, Sort.SHELL);
		for(int i = 0; i < a.length; i++){
			System.out.println(a[i]);
		}
		for(int i = 0; i < b.length; i++){
			System.out.println(b[i]);
		}
		for(int i = 0; i < b.length; i++){
			System.out.println(c[i]);
		}
	}
}