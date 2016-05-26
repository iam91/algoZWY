public class ShellSort{
	public static void sort(Comparable[] a){
		shellSort(a);
	}

	private static void shellSort(Comparable[] a){
		int n = a.length;
		int h = 1;
		int preH = 3 * h + 1;
		while(preH < n / 3){
			h = preH;
			preH = 3 * h + 1;
		}
		while(h > 0){
			for(int i = 0; i < n; i++){
				for(int j = i; j > 0 && SortUtils.less(a[j], a[j - h]); j -= h){
					SortUtils.swap(a, j, j - h);
				}
			}
			h = h / 3;
		}
	}
}