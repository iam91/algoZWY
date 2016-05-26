public class Sort{
	public static final int SELECTION = 1;
	public static final int INSERTION = 2;
	public static final int SHELL = 3;

	public static void sort(Comparable[] a, int sortType){
		switch(sortType){
			case SELECTION:
				selectionSort(a);
				break;
			case INSERTION:
				insertionSort(a);
				break;
			case SHELL:
				shellSort(a);
				break;
			default:
				break;
		}
	}

	private static void selectionSort(Comparable[] a){
		int n = a.length;
		for(int i = 0; i < n; i++){
			int minId = i;
			for(int j = i; j < n; j++){
				if(less(a[j], a[minId])){
					minId = j;
				}
			}
			swap(a, minId, i);
		}
	}

	private static void insertionSort(Comparable[] a){
		int n = a.length;
		for(int i = 0; i < n; i++){
			for(int j = i; j > 0 && less(a[j], a[j - 1]); j--){
				swap(a, j, j - 1);
			}
		}
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
				for(int j = i; j > 0 && less(a[j], a[j - h]); j -= h){
					swap(a, j, j - h);
				}
			}
			h = h / 3;
		}
	}

	private static boolean less(Comparable a, Comparable b){
		return a.compareTo(b) < 0;
	}

	private static void swap(Comparable[] a, int i, int j){
		Comparable t = a[i];
		a[i] = a[j];
		a[j] = t;
	}
}
