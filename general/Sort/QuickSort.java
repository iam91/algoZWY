public class QuickSort{
	public static void sort(Comparable[] a){
		QuickSort(a, 0, a.length - 1);
	}

	private static void QuickSort(Comparable[] a, int l, int r){
		if(r <= l){
			return;
		}
		int pivId = partition(a, l, r);
		QuickSort(a, l, pivId - 1);
		QuickSort(a, pivId + 1, r);
	}

	private static int partition(Comparable[] a, int l, int r){
		if(r <= l){
			return l;
		}
		Comparable piv = a[l];
		int pivId = l;
		int i = l; 
		int j = r;
		while(i < j){
			while(i < j && SortUtils.less(piv, a[j])){
				j--;
			}
			a[pivId] = a[j];
			pivId = j;
			while(i < j && !SortUtils.less(piv, a[i])){
				i++;
			}
			a[pivId] = a[i];
			pivId = i;
		}
		a[pivId] = piv;
		return pivId;
	}
}