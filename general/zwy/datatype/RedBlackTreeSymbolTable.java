package zwy.datatype;

import java.util.Iterator;

public class RedBlackTreeSymbolTable<K extends Comparable<K>, V>
	extends OrderedSymbolTable<K, V>{

	private static final boolean RED = true;
	private static final boolean BLACK = false;

	private Node root;

	public RedBlackTreeSymbolTable(){
		super();
		root = null;
	}

	public void put(K key, V val){
		if(key == null || val == null){
			return;
		}
		root = put(key, val, root);
	}

	private Node put(K key, V val, Node root){
		if(root == null){
			return new Node(key, val, 1, RED);
		}
		int cmp = key.compareTo(root.key);
		if(cmp < 0){
			root.left = put(key, val, root.left);
		}
		else if(cmp > 0){
			root.right = put(key, val, root.right);
		}
		else{
			root.value = val;
		}
		root = fixUp(root);
		root.size = 1 + size(root.left) + size(root.right);
		return root;
	}

	private Node fixUp(Node root){
		if(!isRed(root.left) && isRed(root.right)){
			root = rotateLeft(root);
		}
		if(isRed(root.left) && isRed(root.left.left)){
			root = rotateRight(root);
		}
		if(isRed(root.left) && isRed(root.right)){
			flipColors(root);
		}
		return root;
	}

	private void flipColors(Node root){
		root.color = !root.color;
		if(root.left != null){
			root.left.color = !root.left.color;
		}
		if(root.right != null){
			root.right.color = !root.right.color;
		}
	}

	private Node rotateLeft(Node root){
		Node t = root.right;
		root.right = t.left;
		t.left = root;
		t.color = root.color;
		root.color = RED;
		t.size = root.size;
		root.size = 1 + size(root.left) + size(root.right);
		return t;
	}

	private Node rotateRight(Node root){
		Node t = root.left;
		root.left = t.right;
		t.right = root;
		t.color = root.color;
		root.color = RED;
		t.size = root.size;
		root.size = 1 + size(root.left) + size(root.right);
		return t;
	}

	private int size(Node root){
		return root == null ? 0 : root.size;
	}

	private boolean isRed(Node x){
		return x == null ? false : x.color == RED;
	}

	public V get(K key){
		if(key == null || root == null){
			return null;
		}
		return get(root, key);
	}

	private V get(Node root, K key){
		if(root == null){
			return null;
		}
		int cmp = key.compareTo(root.key);
		if(cmp > 0){
			return get(root.right, key);
		}
		else if(cmp < 0){
			return get(root.left, key);
		}
		else{
			return root.value;
		}
	}

	public void delete(K key){

	}

	public boolean contains(K key){
		return contains(root, key);
	}

	private boolean contains(Node root, K key){
		if(root == null){
			return false;
		}
		int cmp = key.compareTo(root.key);
		if(cmp > 0){
			return contains(root.right, key);
		}
		else if(cmp < 0){
			return contains(root.left, key);
		}
		else{
			return true;
		}
	}

	public K min(){return null;}
	public K max(){return null;}
	public K floor(K key){return null;}
	public K ceiling(K key){return null;}
	public int rank(K key){return 0;}
	public K select(int k){return null;}
	
	public void deleteMin(){
		if(root != null){
			root = deleteMin(root);
		}
	}

	private Node deleteMin(Node root){
		if(root.left == null){
			return null;
		}
		if(!isRed(root.left) && !isRed(root.left.left)){
			root = moveRedLeft(root);
		}
		root.left = deleteMin(root.left);
		root = fixUp(root);
		root.size = 1 + size(root.left) + size(root.right);
		return root;
	}

	private Node moveRedLeft(Node root){
		flipColors(root);
		if(isRed(root.right.left)){
			root.right = rotateRight(root.right);
			root = rotateLeft(root);
			flipColors(root);
		}
		return root;
	} 
	
	public void deleteMax(){
		if(root != null){
			root = deleteMax(root);
			if(!isEmpty()){
				root.color = BLACK;
			}
		}
	}

	private Node deleteMax(Node root){
		if(isRed(root.left)){
			root = rotateRight(root);
		}
		if(root.right == null){
			return null;
		}
		if(!isRed(root.right) && !isRed(root.right.left)){
			root = moveRedRight(root);
		}
		root.right = deleteMax(root.right);
		root.size = size(root.left) + size(root.right) + 1;
		return root;
	}

	private Node moveRedRight(Node root){
		flipColors(root);
		if(isRed(root.left.left)){
			root = rotateRight(root);
			flipColors(root);
		}
		return root;
	}
	
	public int size(K lo, K hi){return 0;}

	public int size(){
		if(root == null){
			return 0;
		}
		return root.size;
	}

	public boolean isEmpty(){
		return root == null;
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

	private int traverse(Node root, Comparable[] arr, int curr, K lo, K hi){
		if(root == null){
			return curr;
		}
		curr = traverse(root.left, arr, curr, null, null);
		if((lo == null && hi == null) 
			|| (lo.compareTo(root.key) <= 0 && hi.compareTo(root.key) >= 0)){
			arr[curr++] = root.key;
		}
		curr = traverse(root.right, arr, curr, null, null);
		return curr;
	}

	public Iterable<K> keys(K lo, K hi){return null;}

	private class Node{
		K key;
		V value;
		Node left, right;
		int size;
		boolean color;

		public Node(K key, V value, int size, boolean color){
			this.key = key; 
			this.value = value;
			this.size = size;
			this.color = color;
			this.left = this.right = null;
		}
	}
}