package zwy.sort;

import zwy.util.Util;

public class SelectionSort{
	public static void sort(Comparable[] a){
		selectionSort(a);
	}

	private static void selectionSort(Comparable[] a){
		int n = a.length;
		for(int i = 0; i < n; i++){
			int minId = i;
			for(int j = i; j < n; j++){
				if(Util.less(a[j], a[minId])){
					minId = j;
				}
			}
			Util.swap(a, minId, i);
		}
	}
}