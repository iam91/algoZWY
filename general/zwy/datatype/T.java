package zwy.datatype;

import java.util.Iterator;

public class T{
	public static void main(String[] args){
		Integer[] f = {1, 5, 7, 0, 2, 6, 9, -1, -3, 45};
		SeperateChainingHashST<Integer, Integer> t
			= new SeperateChainingHashST<Integer, Integer>();

		for(int i = 0; i < 10; i++){
			t.put(f[i], f[i] + 1);
			System.out.print(f[i] + " ");
		}
		System.out.println();

		Iterator<Integer> iter = t.keys().iterator();
		while(iter.hasNext()){
			System.out.print(iter.next() + " ");
		}
		System.out.println();
		System.out.println(t.size());
	}
}