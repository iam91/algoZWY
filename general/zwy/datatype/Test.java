package zwy.datatype;

import java.util.Iterator;

public class Test{
	public static void main(String[] args){
		Integer[] f = {1, 5, 7, 0, 2, 6, 9, -1, -3, 45};
		BSTSymbolTable<Integer, Integer> t 
			= new BSTSymbolTable<Integer, Integer>();
		BinarySearchSymbolTable<Integer, Integer> p
			= new BinarySearchSymbolTable<Integer, Integer>();
		RedBlackTreeSymbolTable<Integer, Integer> r
			= new RedBlackTreeSymbolTable<Integer, Integer>();

		for(int i = 0; i < 10; i++){
			t.put(f[i], f[i] + 1);
			p.put(f[i], f[i] + 1);
			r.put(f[i], f[i] + 1);
			System.out.print(f[i] + " ");
		}
		System.out.println();

		Iterator<Integer> iter = r.keys().iterator();
		while(iter.hasNext()){
			System.out.print(iter.next() + " ");
		}
		System.out.println();
		System.out.println(r.size());

		for(int i = 0; i < 10; i++){
			System.out.print(r.get(f[i]) + " ");
		}
		System.out.println();

		r.deleteMin();
		iter = r.keys().iterator();
		while(iter.hasNext()){
			System.out.print(iter.next() + " ");
		}
		System.out.println();
		System.out.println(r.size());

		r.deleteMax();
		iter = r.keys().iterator();
		while(iter.hasNext()){
			System.out.print(iter.next() + " ");
		}
		System.out.println();
		System.out.println(r.size());

		r.delete(2);
		iter = r.keys().iterator();
		while(iter.hasNext()){
			System.out.print(iter.next() + " ");
		}
		System.out.println();
		System.out.println(r.size());

		r.delete(5);
		iter = r.keys().iterator();
		while(iter.hasNext()){
			System.out.print(iter.next() + " ");
		}
		System.out.println();
		System.out.println(r.size());
	}
}