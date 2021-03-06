package zwy.sort;

public class SortClient{
	public static final int SELECTION = 1;
	public static final int INSERTION = 2;
	public static final int SHELL = 3;
	public static final int MERGE_TOPDOWN = 4;
	public static final int MERGE_BUTTOMUP = 5;
	public static final int QUICK = 6;
	public static final int HEAP = 7;

	public static void sort(Comparable[] a, int sortType){
		switch(sortType){
			case SELECTION:
				SelectionSort.sort(a);
				break;
			case INSERTION:
				InsertionSort.sort(a);
				break;
			case SHELL: 
				ShellSort.sort(a);
				break;
			case MERGE_TOPDOWN:
				MergeSort.sort(a, true);
				break;
			case MERGE_BUTTOMUP:
				MergeSort.sort(a, false);
				break;
			case QUICK:
				QuickSort.sort(a);
				break;
			case HEAP:
				HeapSort.sort(a);
				break;
			default:
				break;
		}
	}
}