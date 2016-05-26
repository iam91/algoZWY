public class InsertionSort{
	public static void sort(Comparable[] a){
		insertionSort(a);
	}

	private static void insertionSort(Comparable[] a){
		int n = a.length;
		for(int i = 0; i < n; i++){
			for(int j = i; j > 0 && SortUtils.less(a[j], a[j - 1]); j--){
				SortUtils.swap(a, j, j - 1);
			}
		}
	}
}