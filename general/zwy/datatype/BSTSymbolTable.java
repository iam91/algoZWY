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
		n = root.size;
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
		return null;
	}

	public K max(){
		return null;
	}
	public K floor(K key){
		return null;
	}
	public K ceiling(K key){
		return null;
	}
	
	public int rank(K key){
		return 0;
	}
	
	public K select(int k){
		return null;
	}
	public void deleteMin(){
		deleteMin(root);
	}

	private Node deleteMin(Node root){
		if(root == null){
			return null;
		}
		else if(root.left == null){
			return root.right;
		}
		else{
			return deleteMin(root.left);
		}
	}

	public void deleteMax(){
		return;
	}
	public int size(K lo, K hi){
		return 0;
	}
	public Iterable<K> keys(){
		return null;
	}
	public Iterable<K> keys(K lo, K hi){
		return null;
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