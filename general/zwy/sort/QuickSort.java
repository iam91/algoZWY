package zwy.sort;

import zwy.util.Util;

import java.util.Random;

public class QuickSort{
	private static Random rand;

	public static void sort(Comparable[] a){
		rand = new Random();
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
		int t = l + rand.nextInt(r - l + 1);
		Util.swap(a, t, l);

		Comparable piv = a[l];
		int i = l;
		int j = r + 1;
		while(true){
			while(!Util.less(piv, a[++i])){
				if(i == r){
					break;
				}
			}
			while(Util.less(piv, a[--j])){
				if(j == l){
					break;
				}
			}
			if(j <= i){
				break;
			}
			Util.swap(a, i, j);
		}
		Util.swap(a, l, j);
		return j;
	}
	/*
	private static int partition(Comparable[] a, int l, int r){
		if(r <= l){
			return l;
		}
		int t = l + rand.nextInt(r - l + 1);
		Util.swap(a, t, l);

		Comparable piv = a[l];
		int pivId = l;
		int i = pivId; 
		int j = r;
		while(i < j){
			while(pivId < j && Util.less(piv, a[j])){
				j--;
			}
			Util.swap(a, j, pivId);
			pivId = j;
			while(i < pivId && !Util.less(piv, a[i])){
				i++;
			}
			Util.swap(a, i, pivId);
			pivId = i;
		}
		return pivId;
	}
	*/
}