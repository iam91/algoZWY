public class SortClient{
	public static final int SELECTION = 1;
	public static final int INSERTION = 2;
	public static final int SHELL = 3;
	public static final int MERGE = 4;

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
			case MERGE:
				MergeSort.sort(a);
				break;
			default:
				break;
		}
	}
}