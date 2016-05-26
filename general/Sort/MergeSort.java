public class MergeSort{
	public static void sort(Comparable[] a){
		int n = a.length;
		Comparable[] b = new Comparable[n];
		mergeSort(a, b, 0, n - 1);
	}

	private static void mergeSort(Comparable[] a, Comparable[] b, int l, int r){
		if(r <= l){
			return;
		}
		int mid = (l + r) / 2;
		mergeSort(a, b, l, mid);
		mergeSort(a, b, mid + 1, r);
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
}