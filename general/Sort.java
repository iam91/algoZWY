public class Sort{
	private static int SELECTION = 1;
	private static int INSERTION = 2;

	public static void sort(Comparable[] a, int sortType){

	}

	private static boolean less(Comparable a, Comparable b){
		return a.compareTo(b) < 0;
	}

	private static void swap(Comparable a, Comparable b){
		Comparable t = a;
		a = b;
		b = t;
	}
}
