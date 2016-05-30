package zwy.sort;

import zwy.util.Util;

public class HeapSort{
	private static int n;

	public static void sort(Comparable[] a){
		n = a.length;
		heapSort(a);
	}

	private static void heapSort(Comparable[] a){
		build(a);
		while(n > 0){
			Util.swap(a, 0, n - 1);
			n--;
			sink(a, 0);
		}
	}

	private static void build(Comparable[] a){
		for(int root = (n - 2) / 2; root >= 0; root--){
			sink(a, root);
		}
	}

	private static void sink(Comparable[] a, int k){
		while(2 * k + 1 < n){
			int next = 2 * k + 1;
			if(next + 1 < n && Util.less(a[next], a[next + 1])){
				next++;
			}
			if(Util.less(a[next], a[k])){
				break;
			}
			Util.swap(a, next, k);
			k = next;
		}
	}
}