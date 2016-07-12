package zwy.datatype;

import java.util.Iterator;

public class T{
	public static void main(String[] args){
		Integer[] f = {1, 5, 7, 0, 119, 2, 6, 9, -1, -3, 45, 23, 19};
		//Integer[] f = {0};
		SeperateChainingHashST<Integer, Integer> t
			= new SeperateChainingHashST<Integer, Integer>(5);

		LinearProbingHashST<Integer, Integer> tt
			= new LinearProbingHashST<Integer, Integer>(4);

		Integer ii = 0;
		System.out.println(ii.hashCode());

		for(int i = 0; i < f.length; i++){
			t.put(f[i], f[i] + 1);
			tt.put(f[i], f[i] + 1);
			System.out.print(f[i] + " ");
		}
		System.out.println();

		Iterator<Integer> iter = tt.keys().iterator();
		while(iter.hasNext()){
			System.out.print(iter.next() + " ");
		}
		System.out.println();
		System.out.println(tt.size());
		System.out.println("=====================================");
		//t.p();
	}
}