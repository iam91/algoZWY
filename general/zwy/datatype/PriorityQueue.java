package zwy.datatype;

import zwy.util.Util;

public class PriorityQueue{

	private Comparable[] pq;
	private int length;
	private int N;

	public PriorityQueue(){
		N = 0;
		pq = new Comparable[2];
	}

	public int size(){
		return N;
	}

	public boolean isEmpty(){
		return N == 0;
	}

	public void insert(Comparable a){
		N++;
		if(N > pq.length - 1){
			Comparable[] newPQ = new Comparable[pq.length * 2 - 1];
			for(int i = 1; i < pq.length; i++){
				newPQ[i] = pq[i];
				pq[i] = null;
			}
			pq = newPQ;
		}
		pq[N] = a;
		swim(N);
	}

	public Comparable max(){
		Comparable ret = N > 0 ? pq[1] : null;
		return ret;
	}

	public Comparable delMax(){
		Comparable ret = max();
		if(N > 0){
			Util.swap(pq, 1, N--);
			sink(1);
			pq[N + 1] = null;
		}
		if(N <= (pq.length - 1) / 4){
			Comparable[] newPQ = new Comparable[pq.length / 2 + 1];
			for(int i = 1; i <= N; i++){
				newPQ[i] = pq[i];
				pq[i] = null;
			}
			pq = newPQ;
		}
		return ret;
	}

	public void pp(){
		System.out.println("--- " + N + "," + (pq.length - 1) + " ---");
	}

	public void p(){
		for(int i = 1; i <= N; i++){
			System.out.println(pq[i]);
		}
	}

	private void swim(int k){
		while(k > 1 && Util.less(pq[k / 2], pq[k])){
			Util.swap(pq, k / 2, k);
			k /= 2;
		}
	}

	private void sink(int k){
		while(k * 2 <= N){
			int next = k * 2;
			if(next < N && Util.less(pq[next], pq[next + 1])){
				next++;
			}
			if(Util.less(pq[next], pq[k])){
				break;
			}
			Util.swap(pq, k, next);
			k = next;
		}
	}
}