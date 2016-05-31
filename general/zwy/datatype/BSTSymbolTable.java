package zwy.datatype;

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
		int cmp = root.key.compareTo(key);
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

	public abstract V get(K key);
	public abstract void delete(K key);
	public abstract boolean contains(K key);
	public abstract K min();
	public abstract K max();
	public abstract K floor(K key);
	public abstract K ceiling(K key);
	public abstract int rank(K key);
	public abstract K select(int k);
	public abstract void deleteMin();
	public abstract void deleteMax();
	public abstract int size(K lo, K hi);
	public abstract Iterable<K> keys();
	public abstract Iterable<K> keys(K lo, K hi);

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