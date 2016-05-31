package zwy.datatype;

import java.util.Iterator;

public class Test{
	public static void main(String[] args){
		SequentialSearchSymbolTable<String, Integer> t = 
			new SequentialSearchSymbolTable<String, Integer>();
		for(int i = 0; i < 10; i++){
			Integer value = i;
			String key = value.toString();
			t.put(key, value);
		}
		for(int i = 0; i < 10; i++){
			Integer ii = i % 2 == 1 ? i : i + 10;
			String key = ii.toString();
			if(t.contains(key)){
				System.out.println(t.get(key));
			}
		}
		System.out.println("---------------");
		for(int i = 0; i < 10; i++){
			Integer ii = i;
			String key = ii.toString();
			if(t.contains(key)){
				System.out.println(t.get(key));
			}
		}
		System.out.println("---------------");
		for(int i = 0; i < 10; i++){
			Integer ii = i % 2 == 1 ? i : i + 10;
			String key = ii.toString();
			if(t.contains(key)){
				System.out.println(key);
				t.delete(key);
			}
		}
		System.out.println("===============");
		for(int i = 0; i < 10; i++){
			Integer ii = i;
			String key = ii.toString();
			if(t.contains(key)){
				System.out.println(t.get(key));
			}
		}
		System.out.println("---------------");
		Iterator<String> iter = t.keys().iterator();
		while(iter.hasNext()){
			System.out.println(iter.next());
		}
		System.out.println("---------------");
		Iterator<String> iter1 = t.keys().iterator();
		while(iter1.hasNext()){
			System.out.println(iter1.next());
		}
		t.put("2", 33);
		System.out.println(t.size() + "+++");
		System.out.println("---------------");
		iter = t.keys().iterator();
		while(iter.hasNext()){
			System.out.println(t.get(iter.next()));
		}
		t.put("22", 22);
		System.out.println(t.size() + "+++");
		System.out.println("---------------");
		iter = t.keys().iterator();
		while(iter.hasNext()){
			System.out.println(t.get(iter.next()));
		}
	}
}