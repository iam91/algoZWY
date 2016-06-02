package zwy.datatype;

import java.util.Iterator;

public class Test{
	public static void main(String[] args){
		Integer[] f = {1, 5, 7, 0, 2, 6, 9, -1, -3, 45};
		BSTSymbolTable<Integer, Integer> t 
			= new BSTSymbolTable<Integer, Integer>();
		BinarySearchSymbolTable<Integer, Integer> p
			= new BinarySearchSymbolTable<Integer, Integer>();
		for(int i = 0; i < 10; i++){
			t.put(f[i], f[i] + 1);
			p.put(f[i], f[i] + 1);
			System.out.print(f[i] + " ");
		}
		System.out.println();
		for(int i = 0; i < 10; i++){
			System.out.print(t.get(f[i]) + " ");
		}
		System.out.println();
		System.out.println(t.size());
		t.delete(0);
		p.delete(0);
		
		for(int i = 0; i < 10; i++){
			System.out.print(t.get(f[i]) + " ");
		}
		System.out.println();
		System.out.println(t.size());
		
		Iterator<Integer> iter = t.keys().iterator();
		while(iter.hasNext()){
			Integer tt = iter.next();
			System.out.print(tt + ":" + t.rank(tt) + ":" + p.rank(tt) + " ");
		}
		System.out.println();
		System.out.println(t.ceiling(0));
		System.out.println(t.floor(6));
		System.out.println(t.size(1, 6));
		System.out.println(p.size(1, 6));
		
		iter = t.keys(0, 6).iterator();
		while(iter.hasNext()){
			System.out.print(iter.next() + " ");
		}
		System.out.println();
		System.out.println(t.min() + ":" + t.max());
		t.deleteMin();
		t.deleteMin();
		t.deleteMax();
		iter = t.keys().iterator();
		while(iter.hasNext()){
			System.out.print(iter.next() + " ");
		}
		System.out.println();
		/*
		for(int i = 0; i < 10; i++){
			System.out.print(t.rank(f[i] + 1) + " ");
		}
		System.out.println();
		for(int i = 0; i < 10; i++){
			int tt = f[i] > 0 ? f[i] : -f[i];
			Integer k = tt % 2 == 0 ? f[i] : f[i] + 1000;
			System.out.print(k + ",");
			if(t.contains(k)){
				System.out.print(t.get(k) + " ");
				t.delete(k);
			}
			else{
				System.out.print("none ");
			}
		}
		System.out.println();
		t.p();
		System.out.println("min " + t.min() + ",max " + t.max());
		System.out.println(t.ceiling(0) + "," + t.floor(0) + " " + t.ceiling(5) + "," + t.floor(5));
		t.deleteMin();
		t.deleteMax();
		t.p();
		System.out.println(t.size() + "," + t.size(0, 7));
		Iterator<Integer> iter = t.keys().iterator();
		while(iter.hasNext()){
			System.out.print(iter.next() + " ");
		}
		System.out.println();
		iter = t.keys(0, 8).iterator();
		while(iter.hasNext()){
			System.out.print(iter.next() + " ");
		}
		System.out.println();
		iter = t.keys().iterator();
		while(iter.hasNext()){
			System.out.print(iter.next() + " ");
		}
		System.out.println();
		iter = t.keys(0, 8).iterator();
		while(iter.hasNext()){
			System.out.print(iter.next() + " ");
		}
		System.out.println();
		*/
	}
}