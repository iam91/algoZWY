package zwy.datatype;

public class Test{
	public static void main(String[] args){
		PriorityQueue pq = new PriorityQueue();

		Integer[] a = {1, 5, 5, 0, 2, 6};
		for(int i = 0; i < a.length; i++){
			pq.insert(a[i]);
			pq.pp();
		}
		System.out.println("-----------");
		while(!pq.isEmpty()){
			System.out.println(pq.delMax());
			pq.pp();
		}
		for(int i = 0; i < a.length; i++){
			pq.insert(a[i]);
			pq.pp();
		}
		System.out.println("-----------");
		while(!pq.isEmpty()){
			System.out.println(pq.delMax());
			pq.pp();
		}
	}
}