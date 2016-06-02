package zwy.datatype;

import java.util.Iterator;

public class BSTSymbolTable<K extends Comparable<K>, V>
	extends OrderedSymbolTable<K, V>{

	private Node root;

	public BSTSymbolTable(){
		super();
		root = null;
	}

	public void put(K key, V val){
		if(key == null || val == null){
			return;
		}
		root =  put(key, val, root);
	}

	private Node put(K key, V val, Node root){
		if(root == null){
			return new Node(key, val, 1);
		}
		int cmp = key.compareTo(root.key);
		if(cmp > 0){
			root.right = put(key, val, root.right);
		}
		else if(cmp < 0){
			root.left = put(key, val, root.left);
		}
		else{
			root.value = val;
		}
		root.size = size(root.left) + size(root.right) + 1;
		return root;
	}

	private int size(Node root){
		if(root == null){
			return 0;
		}
		else{
			return root.size;
		}
	}

	public V get(K key){
		if(key == null){
			return null;
		}
		return get(key, root);
	}

	private V get(K key, Node root){
		if(root == null){
			return null;
		}
		int cmp = key.compareTo(root.key);
		if(cmp < 0){
			return get(key, root.left);
		}
		else if(cmp > 0){
			return get(key, root.right);
		}
		else{
			return root.value;
		}
	}

	public void delete(K key){
		if(key == null){
			return;
		}
		root = delete(key, root);
	}

	private Node delete(K key, Node root){
		if(root == null){
			return null;
		}
		int cmp = key.compareTo(root.key);
		if(cmp > 0){
			root.right = delete(key, root.right);
		}
		else if(cmp < 0){
			root.left = delete(key, root.left);
		}
		else{
			if(root.left == null){
				root = root.right;
			}
			else if(root.right == null){
				root = root.left;
			}
			else{
				Node rightMinNode = min(root.right);
				rightMinNode.right = deleteMin(root.right);
				rightMinNode.left = root.left;
				root = rightMinNode;
			}
		}
		root.size = size(root.left) + size(root.right) + 1;
		return root;
	}

	private Node min(Node root){
		if(root == null){
			return null;
		}
		else if(root.left == null){
			return root;
		}
		else{
			return min(root.left);
		}
	}

	private Node max(Node root){
		if(root == null){
			return null;
		}
		else if(root.right == null){
			return root;
		}
		else{
			return max(root.right);
		}
	}

	public boolean contains(K key){
		return contains(key, root);
	}

	private boolean contains(K key, Node root){
		if(root == null){
			return false;
		}
		int cmp = key.compareTo(root.key);
		if(cmp > 0){
			return contains(key, root.right);
		}
		else if(cmp < 0){
			return contains(key, root.left);
		}
		else{
			return true;
		}
	}

	public K min(){
		Node minNode = min(root);
		if(minNode != null){
			return minNode.key;
		}
		else{
			return null;
		}
	}

	public K max(){
		Node maxNode = max(root);
		if(maxNode != null){
			return maxNode.key;
		}
		else{
			return null;
		}
	}
	
	public K floor(K key){
		if(key == null){
			return null;
		}
		Node f = floor(key, root);
		if(f == null){
			return null;
		}
		else{
			return f.key;
		}
	}

	private Node floor(K key, Node root){
		if(root == null){
			return null;
		}
		int cmp = key.compareTo(root.key);
		if(cmp > 0){
			Node t = floor(key, root.right);
			if(t == null){
				return root;
			}
			else{
				return t;
			}
		}
		else if(cmp < 0){
			return floor(key, root.left);
		}
		else{
			return root;
		}
	}

	public K ceiling(K key){
		if(root == null){
			return null;
		}
		Node c = ceiling(key, root);
		if(c == null){
			return null;
		}
		else{
			return c.key;
		}
	}

	private Node ceiling(K key, Node root){
		if(root == null){
			return null;
		}
		int cmp = key.compareTo(root.key);
		if(cmp > 0){
			return ceiling(key, root.right);
		}
		else if(cmp < 0){
			Node t = ceiling(key, root.left);
			if(t == null){
				return root;
			}
			else{
				return t;
			}
		}
		else{
			return root;
		}
	}
	
	public int rank(K key){
		if(key == null){
			return 0;
		}
		return rank(key, root);
	}

	private int rank(K key, Node root){
		if(root == null){
			return 0;
		}
		int cmp = key.compareTo(root.key);
		if(cmp > 0){
			return size(root.left) + 1 + rank(key, root.right);
		}
		else if(cmp < 0){
			return rank(key, root.left);
		}
		else{
			return size(root.left);
		}
	}
	
	public K select(int k){
		return select(k, root);
	}

	private K select(int k, Node root){
		if(root == null){
			return null;
		}
		int sizeLeft = size(root.left);
		if(sizeLeft > k){
			return select(k, root.left);
		}
		else if(sizeLeft < k){
			return select(k, root.right);
		}
		else{
			return root.key;
		}
	}

	public void deleteMin(){
		root = deleteMin(root);
	}

	private Node deleteMin(Node root){
		if(root == null){
			return null;
		}
		else if(root.left == null){
			return root.right;
		}
		else{
			root.left = deleteMin(root.left);
			root.size = size(root.left) + size(root.right) + 1;
			return root;
		}
	}

	public void deleteMax(){
		root = deleteMax(root);
	}

	private Node deleteMax(Node root){
		if(root == null){
			return null;
		}
		else if(root.right == null){
			return root.left;
		}
		else{
			root.right = deleteMax(root.right);
			root.size = size(root.left) + size(root.right) + 1;
			return root;
		}
	}

	public int size(K lo, K hi){
		if(lo == null || hi == null || hi.compareTo(lo) <= 0){
			return 0;
		}
		int rlo = rank(lo, root);
		int rhi = rank(hi, root);
		Node ceiling = ceiling(lo, root);
		if(ceiling != null && ceiling.key.compareTo(hi) == 0){
			rhi++;
		}
		return rhi - rlo + 1;
	}

	public int size(){
		if(root == null){
			return 0;
		}
		return root.size;
	}

	public Iterable<K> keys(){

		if(root == null){
			return null;
		}
		K[] arr = (K[])new Comparable[root.size];
		traverse(root, arr, 0, null, null);

		return new Iterable<K>(){
			public Iterator<K> iterator(){
				return new Iterator<K>(){

					private int curr = 0;

					public boolean hasNext(){
						return curr < arr.length;
					}

					public K next(){
						return arr[curr++];
					}

					public void remove(){

					}
				};
			}
		};
	}

	public Iterable<K> keys(K lo, K hi){
		if(root == null || lo == null || hi == null
			|| hi.compareTo(lo) <= 0){
			return null;
		}
		int rangeSize = size(lo, hi);
		K[] arr = (K[])new Comparable[rangeSize];
		traverse(root, arr, 0, lo, hi);

		return new Iterable<K>(){
			public Iterator<K> iterator(){
				return new Iterator<K>(){

					private int curr = 0;

					public boolean hasNext(){
						return curr < arr.length;
					}

					public K next(){
						return arr[curr++];
					}

					public void remove(){

					}
				};
			}
		};
	}

	private int traverse(Node root, K[] arr, int curr, K lo, K hi){
		if(root == null){
			return curr;
		}
		curr = traverse(root.left, arr, curr, lo, hi);
		if((lo == null && hi == null) 
			|| (lo.compareTo(root.key) <= 0 && hi.compareTo(root.key) >= 0)){
			arr[curr++] = root.key;
		}
		curr = traverse(root.right, arr, curr, lo, hi);
		return curr;
	}

	private class Node{
		K key;
		V value;
		int size;
		Node left, right;

		public Node(K key, V value, int size){
			this.key = key;
			this.value = value;
			this.size = size;
			this.left = null;
			this.right = null;
		}
	}
}