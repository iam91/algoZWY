public class SelectionSort{
	public static void sort(Comparable[] a){
		selectionSort(a);
	}

	private static void selectionSort(Comparable[] a){
		int n = a.length;
		for(int i = 0; i < n; i++){
			int minId = i;
			for(int j = i; j < n; j++){
				if(SortUtils.less(a[j], a[minId])){
					minId = j;
				}
			}
			SortUtils.swap(a, minId, i);
		}
	}
}