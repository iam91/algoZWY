public class MergeSort{
	public static void sort(Comparable[] a, boolean isTopDown){
		int n = a.length;
		Comparable[] b = new Comparable[n];
		if(isTopDown){
			mergeSortTopDown(a, b, 0, n - 1);
		}
		else{
			mergeSortButtomUp(a, b);
		}
	}

	private static void merge(Comparable[] a, Comparable[] b, int l, int r, int mid){
		int lHead = l;
		int rHead = mid + 1;
		int head = l;
		while(head <= r){
			if(rHead > r || (lHead <= mid && SortUtils.less(a[lHead], a[rHead]))){
				b[head++] = a[lHead++];
			}
			else if(lHead > mid || (rHead <= r && !SortUtils.less(a[lHead], a[rHead]))){
				b[head++] = a[rHead++];
			}
		}
		for(int i = l; i <= r; i++){
			a[i] = b[i];
		}
	}

	private static void mergeSortTopDown(Comparable[] a, Comparable[] b, int l, int r){
		if(r <= l){
			return;
		}
		int mid = (l + r) / 2;
		mergeSortTopDown(a, b, l, mid);
		mergeSortTopDown(a, b, mid + 1, r);
		merge(a, b, l, r, mid);
	}

	private static void mergeSortButtomUp(Comparable[] a, Comparable[] b){
		int n = a.length;
		for(int sz = 1; sz < n; sz *= 2){
			int dsz = sz * 2;
			for(int i = 0; i + sz < n; i += dsz){
				int l = i; 
				int r = i + 2 * sz - 1;
				int mid = l + sz - 1;
				r = r < n ? r : n - 1;
				merge(a, b, l, r, mid);
			}
		}
	}
}